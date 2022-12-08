from fastapi import APIRouter, Depends
from typing import List

from app.cruds.users_cruds import store_profile_url
from app.helpers.user_helpers import (
    create_wallet_for_new_user,
    get_wallet_info,
    hash_password,
    send_login_notification_to_backoffice,
    withdraw_funds_from_user_wallet,
)
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
        raise HTTPException(status_code=403, detail="Incorrect username or password")
    if user_db.blocked:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User blocked by admin"
        )
    hashed_password = hash_password(user.password)
    users_cruds.validate_user(user.email, hashed_password, db)

    send_login_notification_to_backoffice("mailpassword")

    return users_cruds.user_schemas.UserSchema.from_orm(user_db)


@router.post("/signup", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def user_signup(user: UserSignUpSchema, db: Session = Depends(get_db)):
    user_db = users_cruds.get_user_by_email(user.email, db)
    if user_db:
        raise HTTPException(status_code=409, detail="The user already exists")
    created_user, user_id = users_cruds.register_user(user, db)
    create_wallet_for_new_user(user_id)
    return created_user


@router.get("/", response_model=List[UserSchema], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return users_cruds.get_users_from_db(db)


@router.get("/blocked", status_code=status.HTTP_200_OK)
def get_blocked_users_count(db: Session = Depends(get_db)):
    return users_cruds.get_blocked_users_count(db)


@router.get(
    "/blocked/{user_email}",
    response_model=UserIsBlocked,
    status_code=status.HTTP_200_OK,
)
def is_block_user(user_email: EmailStr, db: Session = Depends(get_db)):
    user_db = users_cruds.get_user_by_email(user_email, db)
    if not user_db:
        raise HTTPException(status_code=403, detail="Incorrect username or password")
    return {"is_blocked": user_db.blocked}


@router.post("/blocked/{user_email}", status_code=status.HTTP_200_OK)
def block_user(user_email: EmailStr, db: Session = Depends(get_db)):
    user_db = users_cruds.get_user_by_email(user_email, db)
    if not user_db:
        raise HTTPException(status_code=403, detail="Incorrect username or password")
    if user_db.blocked:
        raise HTTPException(status_code=403, detail="The user is already blocked")
    users_cruds.block_user(user_db, db)
    return "User blocked"


@router.post("/unblocked/{user_email}", status_code=status.HTTP_200_OK)
def unblock_user(user_email: EmailStr, db: Session = Depends(get_db)):
    user_db = users_cruds.get_user_by_email(user_email, db)
    if not user_db:
        raise HTTPException(status_code=403, detail="Incorrect username or password")
    if not user_db.blocked:
        raise HTTPException(status_code=403, detail="The user is already unblocked")
    users_cruds.unblock_user(user_db, db)
    return "User unblocked"


@router.get("/{user_email}/wallet", status_code=status.HTTP_200_OK)
def get_user_wallet(user_email: EmailStr, db: Session = Depends(get_db)):
    user_db = users_cruds.get_user_by_email(user_email, db)
    if not user_db:
        raise HTTPException(status_code=403, detail="Incorrect username")
    if user_db.blocked:
        raise HTTPException(status_code=403, detail="The user is already blocked")

    return get_wallet_info(user_db.user_id)


@router.post("/{user_email}/wallet/withdrawals", status_code=status.HTTP_200_OK)
def withdraw_funds_from_wallet(
    user_email: EmailStr,
    withdrawal_info: WalletWithdrawalSchema,
    db: Session = Depends(get_db),
):
    user_db = users_cruds.get_user_by_email(user_email, db)
    if not user_db:
        raise HTTPException(status_code=403, detail="Incorrect username")
    if user_db.blocked:
        raise HTTPException(status_code=403, detail="The user is already blocked")
    return withdraw_funds_from_user_wallet(user_db.user_id, withdrawal_info)


@router.post("/{user_email}/wallet/withdrawals", status_code=status.HTTP_200_OK)
def withdraw_funds_from_wallet(
    user_email: EmailStr,
    withdrawal_info: WalletWithdrawalSchema,
    db: Session = Depends(get_db),
):
    user_db = users_cruds.get_user_by_email(user_email, db)
    if not user_db:
        raise HTTPException(status_code=403, detail="Incorrect username")
    if user_db.blocked:
        raise HTTPException(status_code=403, detail="The user is already blocked")
    return withdraw_funds_from_user_wallet(user_db.user_id, withdrawal_info)


@router.get("/{user_email}/id", status_code=status.HTTP_200_OK)
def get_user_id_from_email(user_email: EmailStr, db: Session = Depends(get_db)):
    user_db = users_cruds.get_user_by_email(user_email, db)
    if not user_db:
        raise HTTPException(status_code=403, detail="Incorrect username")
    return user_db.user_id


@router.patch("/picture/{useremail}", status_code=status.HTTP_200_OK)
def update_passenger_picture(
    useremail: str, photo: UserPhoto, db: Session = Depends(get_db)
):
    url = photo.photo_url
    store_profile_url(useremail, url, db)
    return {"url": url}
