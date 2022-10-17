from pydantic import BaseModel, EmailStr


class DriverVehicle(BaseModel):
    email: EmailStr
    licence_plate: str
    model: str


class DriverProfile(BaseModel):
    username: str
    surname: str
    ratings: float
    licence_plate: str
    model: str


class DriverAvailability(BaseModel):
    email: str
    username: str
    surname: str
    ratings: float
    licence_plate: str
    model: str


class DriverSelfProfile(BaseModel):
    email: str
    username: str
    surname: str
    ratings: float
    licence_plate: str
    model: str
