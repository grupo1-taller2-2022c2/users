from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
from app.helpers.user_helpers import hash_password

from starlette import status
from app.cruds.users_cruds import *
from app.schemas.users_schemas import *
from app.database import get_db

router = APIRouter()


@router.post("/grantaccess", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def should_grant_access(user: UserSignInSchema, db: Session = Depends(get_db)):
    user_db = get_user_by_email(user.email, db)
    if not user_db:
        raise HTTPException(
            status_code=403, detail="Incorrect username or password")
    if user_db.blocked:
        raise HTTPException(
            status_code=403, detail="The user has been blocked by the admin")
    hashed_password = hash_password(user.password)
    validate_user(user.email, hashed_password, db)
    return user_schemas.UserSchema.from_orm(user_db)


@router.post("/signup", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def user_signup(user: UserSignUpSchema, db: Session = Depends(get_db)):
    user_db = get_user_by_email(user.email, db)
    if user_db:
        raise HTTPException(status_code=409, detail="The user already exists")
    return register_user(user, db)


@router.get("/", response_model=List[UserSchema], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return get_users_from_db(db)
