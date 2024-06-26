import app.models.users_models as users_models
import app.schemas.users_schemas as user_schemas
from app.cruds.passengers_cruds import create_passenger
from pydantic import EmailStr
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.helpers.user_helpers import hash_password, send_reg_notification_to_backoffice


def get_user_by_email(user_email: EmailStr, db: Session):
    return (
        db.query(users_models.User)
        .filter(users_models.User.email == user_email)
        .first()
    )


def validate_user(user_email: EmailStr, hashed_password: str, db: Session):
    user = get_user_by_email(user_email, db)
    if not user or (user.password != hashed_password):
        raise HTTPException(status_code=403, detail="Incorrect mail or password")


def register_user(user: user_schemas.UserSignUpSchema, db: Session):
    db_user = users_models.User(
        email=user.email,
        password=hash_password(user.password),
        username=user.username,
        surname=user.surname,
        blocked=False,
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        create_passenger(db_user.user_id, db)
        send_reg_notification_to_backoffice(user.type_signup)

        return user_schemas.UserSchema.from_orm(db_user), db_user.user_id
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


def get_users_from_db(db: Session):
    users = db.query(users_models.User).all()
    return users


def block_user(user_db: users_models.User, db: Session):
    user_db.blocked = True
    db.commit()


def unblock_user(user_db: users_models.User, db: Session):
    user_db.blocked = False
    db.commit()


def get_data_by_id(user_id: int, db: Session):
    user_db = (
        db.query(users_models.User).filter(users_models.User.user_id == user_id).first()
    )
    return user_db.email, user_db.username, user_db.surname, user_db.photo, user_db.blocked


def get_user_by_id(user_id: int, db: Session):
    return (
        db.query(users_models.User).filter(users_models.User.user_id == user_id).first()
    )


def get_blocked_users_count(db: Session):
    return db.query(users_models.User).filter(users_models.User.blocked == True).count()


def delete_added_users(db: Session):
    try:
        db.query(users_models.User).filter(users_models.User.user_id >= 6).delete()
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not delete users: " + str(e))


def store_profile_url(useremail, photo_url, db: Session):
    user = (
        db.query(users_models.User).filter(users_models.User.email == useremail).first()
    )
    if not user:
        raise HTTPException(status_code=404, detail="The user doesnt exist")
    try:
        user.photo = photo_url
        db.commit()
        return
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")
