from fastapi import APIRouter, Depends
from typing import List
from app.helpers.user_helpers import hash_password
from fastapi import HTTPException
from starlette import status
from app.cruds import users_cruds
from app.schemas.users_schemas import *
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/grantaccess", response_model=UserSchema, status_code=status.HTTP_200_OK)
def grant_access(user: UserSignInSchema, db: Session = Depends(get_db)):
    user_db = users_cruds.get_user_by_email(user.email, db)
    if not user_db:
        raise HTTPException(
            status_code=403, detail="Incorrect username or password")
    if user_db.blocked:
        raise HTTPException(
            status_code=403, detail="The user has been blocked by the admin")
    hashed_password = hash_password(user.password)
    users_cruds.validate_user(user.email, hashed_password, db)
    return users_cruds.user_schemas.UserSchema.from_orm(user_db)


@router.post("/signup", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def user_signup(user: UserSignUpSchema, db: Session = Depends(get_db)):
    user_db = users_cruds.get_user_by_email(user.email, db)
    if user_db:
        raise HTTPException(status_code=409, detail="The user already exists")
    return users_cruds.register_user(user, db)


@router.get("/", response_model=List[UserSchema], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return users_cruds.get_users_from_db(db)


@router.post("/blocked/{user_email}", status_code=status.HTTP_200_OK)
def block_user(user_email: EmailStr, db: Session = Depends(get_db)):
    user_db = users_cruds.get_user_by_email(user_email, db)
    if not user_db:
        raise HTTPException(
            status_code=403, detail="Incorrect username or password")
    if user_db.blocked:
        raise HTTPException(
            status_code=403, detail="The user is already blocked")
    users_cruds.block_user(user_db, db)
    return "User blocked"


@router.post("/unblocked/{user_email}", status_code=status.HTTP_200_OK)
def unblock_user(user_email: EmailStr, db: Session = Depends(get_db)):
    user_db = users_cruds.get_user_by_email(user_email, db)
    if not user_db:
        raise HTTPException(
            status_code=403, detail="Incorrect username or password")
    if not user_db.blocked:
        raise HTTPException(
            status_code=403, detail="The user is already unblocked")
    users_cruds.unblock_user(user_db, db)
    return "User unblocked"
