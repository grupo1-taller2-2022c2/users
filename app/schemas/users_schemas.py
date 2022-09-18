from pydantic import BaseModel, Field, EmailStr


class UserSignIn(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
