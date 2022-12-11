from typing import Union
from pydantic import BaseModel, EmailStr


class UserSignInSchema(BaseModel):
    email: EmailStr
    password: str


class UserSignUpSchema(BaseModel):
    email: EmailStr
    password: str
    username: str
    surname: str
    type_signup: str = "mailpassword"


class UserProfile(BaseModel):
    username: str
    surname: str

    class Config:
        orm_mode = True


class DriverInfo(BaseModel):
    rating: float
    licence_plate: str
    model: str


class UserFullInfo(BaseModel):
    email: EmailStr
    username: str
    surname: str
    blocked: bool
    ratings: float
    driver: Union[DriverInfo, None]

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    email: EmailStr
    username: str
    surname: str
    blocked: bool

    class Config:
        orm_mode = True


class UserIsBlocked(BaseModel):
    is_blocked: bool


class WalletWithdrawalSchema(BaseModel):
    user_external_wallet_address: str
    amount_in_ethers: str


class UserPhoto(BaseModel):
    photo_url: str
