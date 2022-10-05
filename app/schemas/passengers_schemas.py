from pydantic import BaseModel, EmailStr


class PassengerAddress(BaseModel):
    email: EmailStr
    street_name: str
    street_number: int
