from pydantic import BaseModel, EmailStr


class PassengerAddress(BaseModel):
    email: EmailStr
    street_name: str
    street_number: int


class PassengerProfile(BaseModel):
    username: str
    surname: str
    ratings: float


class PassengerSelfProfile(BaseModel):
    email: str
    username: str
    surname: str
    ratings: float
