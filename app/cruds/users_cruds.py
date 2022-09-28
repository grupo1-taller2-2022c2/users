from app.models.users_models import User
from app.schemas.users_schemas import User, UserSignUp
from app.routes.users_routes import hash_password
from app.cruds.passengers_cruds import create_passenger
from pydantic import EmailStr
from sqlalchemy.orm import Session
from fastapi import HTTPException


def get_user(user_email: EmailStr, db: Session):
    return db.query(User).filter(User.email == user_email).first()


def validate_user(user_email: EmailStr, password: int, db: Session):
    user = get_user(user_email, db)
    if not user or (user.password != password):
        raise HTTPException(
            status_code=403, detail="Incorrect mail or password")


def register_user(user: UserSignUp, db: Session):
    db_user = User(
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
        create_passenger(db_user.id, db)
        return User
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


def get_users_from_db(db: Session):
    users = db.query(User).all()
    return users
