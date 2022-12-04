from pydantic import BaseModel, EmailStr


class UserSignInSchema(BaseModel):
    email: EmailStr
    password: str


class UserSignUpSchema(BaseModel):
    email: EmailStr
    password: str
    username: str
    surname: str


class UserProfile(BaseModel):
    username: str
    surname: str

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    email: EmailStr
    username: str
    surname: str

    class Config:
        orm_mode = True


class UserIsBlocked(BaseModel):
    is_blocked: bool


class WalletWithdrawalSchema(BaseModel):
    user_external_wallet_address: str
    amount_in_ethers: str


class UserPhoto(BaseModel):
    photo_url: str
