from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from app.cruds.users_cruds import get_user_by_email, get_email_by_id
from app.cruds.drivers_cruds import *
from app.schemas.drivers_schemas import *
from app.database import get_db
from typing import List

router = APIRouter()


@router.post("/vehicle", status_code=status.HTTP_201_CREATED)
def add_vehicle(vehicle: DriverVehicle, db: Session = Depends(get_db)):
    db_user = get_user_by_email(vehicle.email, db)
    if not db_user:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    return add_vehicle_to_db(vehicle, db_user.user_id, db)


@router.get("/all_available", response_model=List[DriverAvailability], status_code=status.HTTP_200_OK)
def available_drivers(db: Session = Depends(get_db)):
    db_drivers = get_available_drivers(db)
    response = []
    for driver in db_drivers:
        user_id = driver.user_id
        db_vehicle = get_driver_vehicle(user_id, db)
        email = get_email_by_id(user_id, db)
        response.append({"email": email,
                         "ratings": driver.ratings,
                         "licence_plate": db_vehicle.licence_plate,
                         "model": db_vehicle.model})
    return response


@router.get("/{useremail}", response_model=DriverProfile, status_code=status.HTTP_200_OK)
def get_user(useremail: str, db: Session = Depends(get_db)):
    user_db = get_user_by_email(useremail, db)
    if not user_db:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    driver_db = get_driver_profile(user_db.user_id, db)
    if not driver_db:
        raise HTTPException(
            status_code=404, detail="The driver doesn't exist")
    vehicle_db = get_driver_vehicle(user_db.user_id, db)
    profile = {
        "username": user_db.username,
        "surname": user_db.surname,
        "ratings": driver_db.ratings,
        "licence_plate": vehicle_db.licence_plate,
        "model": vehicle_db.model
    }
    return profile


@router.get("/me/{useremail}", response_model=DriverSelfProfile, status_code=status.HTTP_200_OK)
def get_user(useremail: str, db: Session = Depends(get_db)):
    user_db = get_user_by_email(useremail, db)
    if not user_db:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    driver_db = get_driver_profile(user_db.user_id, db)
    if not driver_db:
        raise HTTPException(
            status_code=404, detail="The driver doesn't exist")
    vehicle_db = get_driver_vehicle(user_db.user_id, db)
    profile = {
        "email": useremail,
        "username": user_db.username,
        "surname": user_db.surname,
        "ratings": driver_db.ratings,
        "licence_plate": vehicle_db.licence_plate,
        "model": vehicle_db.model
    }
    return profile
