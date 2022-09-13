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


@router.get("/signin",  status_code=status.HTTP_200_OK)
def user_signin(user: UserSignIn, db: Session = Depends(get_db)):
    return validate_user(user.email, user.password, db)
