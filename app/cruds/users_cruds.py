from app.models.users_models import User, Address
from app.schemas.users_schemas import User, UserAddress, UserSignUp
from pydantic import EmailStr

from sqlalchemy.orm import Session

from fastapi import HTTPException


def get_user(user_email: EmailStr, db: Session):
    return db.query(User).filter(User.email == user_email).first()


def validate_user(user_email: EmailStr, user_password: str, db: Session):
    user = get_user(user_email, db)
    if not user or (user.password != user_password):
        raise HTTPException(
            status_code=403, detail="Incorrect mail or password")
    return "Todo OK"


def register_user(user: UserSignUp, db: Session):
    db_user = User(
        email=user.email,
        password=user.password,
        username=user.username,
        surname=user.surname,
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return User
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


def add_pred_address(user: UserAddress, db: Session):
    db_user = get_user(user.email, db)
    if not db_user:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    db_address = Address(
        email=user.email,
        street_name=user.street_name,
        street_number=user.street_number,
    )
    try:
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


def get_users_from_db(db: Session):
    users = db.query(User).all()
    return users
