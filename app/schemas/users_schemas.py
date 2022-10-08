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
