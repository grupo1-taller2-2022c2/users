from pydantic import BaseModel, EmailStr


class UserSignInSchema(BaseModel):
    email: EmailStr
    password: str


class UserSignUpSchema(BaseModel):
    email: EmailStr
    password: str
    username: str
    surname: str


class UserSchema(BaseModel):
    email: EmailStr
    password: str
    username: str
    surname: str

    class Config:
        orm_mode = True
