from app.models.users_models import User
from pydantic import EmailStr

from sqlalchemy.orm import Session

from fastapi import HTTPException


def validate_user(user_email: EmailStr, password: str, db: Session):
    user = db.query(User).filter(User.email == user_email).first()
    if not user or (user.password != password):
        raise HTTPException(
            status_code=403, detail="Incorrect mail or password")
    return "Todo OK"


def get_users_from_db(db: Session):
    users = db.query(User).all()
    return users
