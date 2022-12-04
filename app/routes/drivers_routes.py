from fastapi import APIRouter, Depends, HTTPException, File
from starlette import status
from app.cruds.users_cruds import get_user_by_email, get_data_by_id
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
        email, username, surname = get_data_by_id(user_id, db)
        response.append({"email": email,
                         "username": username,
                         "surname": surname,
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
    ratings = get_driver_average_ratings(useremail, db)
    photo = user_db.photo
    if photo is None:
        photo = "https://firebasestorage.googleapis.com/v0/b/fiuber-365100.appspot.com/o/user.jpg?alt=media&token=2f59f69b-124a-4431-9091-48ea98d57c25"
    profile = {
        "username": user_db.username,
        "surname": user_db.surname,
        "ratings": ratings,
        "licence_plate": vehicle_db.licence_plate,
        "model": vehicle_db.model,
        "photo": photo
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
    ratings = get_driver_average_ratings(useremail, db)
    photo = user_db.photo
    if photo is None:
        photo = "https://firebasestorage.googleapis.com/v0/b/fiuber-365100.appspot.com/o/user.jpg?alt=media&token=2f59f69b-124a-4431-9091-48ea98d57c25"
    profile = {
        "email": useremail,
        "username": user_db.username,
        "surname": user_db.surname,
        "ratings": ratings,
        "licence_plate": vehicle_db.licence_plate,
        "model": vehicle_db.model,
        "photo": photo
    }
    return profile


@router.patch("/{useremail}", status_code=status.HTTP_200_OK)
def update_driiver_profile(useremail: str, user: DriverProfile, db: Session = Depends(get_db)):
    user_db = get_user_by_email(useremail, db)
    if not user_db:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    return update_driiver_profile_db(user, user_db, db)


@router.post("/ratings", status_code=status.HTTP_201_CREATED)
def user_add_driver_ratings(rating: DriverRating, db: Session = Depends(get_db)):
    """Add a rating to the driver"""
    db_user = get_user_by_email(rating.driver_email, db)
    if not db_user:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    return add_driver_rating(rating.driver_email, rating.trip_id, rating.ratings, rating.message, db)


@router.get("/ratings/all/{useremail}", status_code=status.HTTP_200_OK)
def user_get_driver_ratings(useremail: str, db: Session = Depends(get_db)):
    db_user = get_user_by_email(useremail, db)
    if not db_user:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    return get_all_driver_ratings(useremail, db)


@router.get("/ratings/{ratings_id}", status_code=status.HTTP_200_OK)
def user_get_driver_rating(ratings_id: int, db: Session = Depends(get_db)):
    return get_driver_ratings(ratings_id, db)


@router.post("/reports", status_code=status.HTTP_201_CREATED)
def report_driver(report: DriverReport, db: Session = Depends(get_db)):
    db_passenger = get_user_by_email(report.passenger_email, db)
    if not db_passenger:
        raise HTTPException(
            status_code=404, detail="The passenger doesn't exist")
    return add_report(report, db)


@router.delete("/reports", status_code=status.HTTP_200_OK)
def delete_report_with_report_id(report: ReportDelete, db: Session = Depends(get_db)):
    return delete_report(report.report_id, db)


@router.get("/reports/all", status_code=status.HTTP_200_OK)
def get_drivers_reports(db: Session = Depends(get_db)):
    return get_all_reports(db)
