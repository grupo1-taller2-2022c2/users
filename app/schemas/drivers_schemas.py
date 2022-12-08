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
    photo: str


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
    photo: str


class DriverRating(BaseModel):
    driver_email: str
    trip_id: int
    ratings: int
    message: str


class DriverReport(BaseModel):
    driver_email: str
    passenger_email: str
    trip_id: int
    reason: str


class ReportDelete(BaseModel):
    report_id: int
