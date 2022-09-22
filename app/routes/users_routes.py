from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlalchemy.orm import Session
from starlette import status

from ..database import SessionLocal

from ..cruds.users_cruds import *

from ..schemas.users_schemas import *

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/signin",  status_code=status.HTTP_200_OK)
def user_signin(user: UserSignIn, db: Session = Depends(get_db)):
    return validate_user(user.email, user.password, db)


@router.get("/", response_model=List[User], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return get_users_from_db(db)


@router.post("/signup", response_model=User, status_code=status.HTTP_201_CREATED)
def user_signup(user: UserSignUp, db: Session = Depends(get_db)):
    user_db = get_user(user.email, db)
    if user_db:
        raise HTTPException(status_code=409, detail="The user already exists")
    return register_user(user, db)


@router.post("/address", status_code=status.HTTP_200_OK)
def user_add_pred_address(user: UserAddress, db: Session = Depends(get_db)):
    return add_pred_address(user, db)


# @router.post("/vehicle", status_code=status.HTTP_200_OK)
