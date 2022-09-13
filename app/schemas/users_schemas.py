from pydantic import BaseModel, Field, EmailStr


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
