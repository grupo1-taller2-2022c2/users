from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
from app.helpers.user_helpers import hash_password

from starlette import status
from app.cruds.users_cruds import *
from app.schemas.users_schemas import *
from app.database import get_db

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):

    user = fake_decode_token(token, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def get_current_active_user(current_user: UserSchema = Depends(get_current_user)):
    if False:  # current_user.disabled:  # TODO: campo disabled todavia no existe
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# form_data.username is the email of the user!


@router.post("/token",  status_code=status.HTTP_200_OK)
def user_signin(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_db = get_user_by_email(form_data.username, db)
    if not user_db:
        raise HTTPException(
            status_code=403, detail="Incorrect username or password")
    if user_db.blocked:
        raise HTTPException(
            status_code=403, detail="The user has been blocked by the admin")
    hashed_password = hash_password(form_data.password)
    validate_user(form_data.username, hashed_password, db)
    # Habilita al usuario en la base de datos
    return {"access_token": user_db.email, "token_type": "bearer"}


@router.get("/me")
def read_users_me(current_user: UserSchema = Depends(get_current_active_user)):
    return current_user
