from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
from app.helpers.user_helpers import hash_password

from starlette import status
from app.cruds.users_cruds import *
from app.schemas.users_schemas import *
from app.database import get_db

router = APIRouter()


@router.post("/token",  status_code=status.HTTP_200_OK)
def user_signin(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_db = get_user(form_data.username, db)
    if not user_db:
        raise HTTPException(
            status_code=403, detail="Incorrect username or password")
    if user_db.blocked:
        raise HTTPException(
            status_code=403, detail="The user has been blocked by the admin")
    hashed_password = hash_password(form_data.password)
    validate_user(form_data.username, hashed_password, db)
    return {"access_token": user_db.username, "token_type": "bearer"}


@router.get("/", response_model=List[User], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return get_users_from_db(db)


@router.post("/signup", response_model=User, status_code=status.HTTP_201_CREATED)
def user_signup(user: UserSignUp, db: Session = Depends(get_db)):
    user_db = get_user(user.email, db)
    if user_db:
        raise HTTPException(status_code=409, detail="The user already exists")
    return register_user(user, db)
