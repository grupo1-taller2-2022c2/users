from pydantic import BaseModel, EmailStr


class DriverVehicle(BaseModel):
    email: EmailStr
    licence_plate: str
    model: str
