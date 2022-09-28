from pydantic import BaseModel, EmailStr


class UserSignIn(BaseModel):
    email: EmailStr
    password: str


class UserSignUp(BaseModel):
    email: EmailStr
    password: str
    username: str
    surname: str


class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    surname: str

    class Config:
        orm_mode = True
