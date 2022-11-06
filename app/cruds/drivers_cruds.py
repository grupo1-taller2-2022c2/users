from app.models.drivers_models import Driver, Vehicle, DriverRating
from app.schemas.drivers_schemas import DriverVehicle, DriverProfile
import app.models.drivers_models as drivers_models
from app.cruds.users_cruds import get_user_by_id
from sqlalchemy.orm import Session
from fastapi import HTTPException


def create_driver(user_id: int, db: Session):
    db_driver = Driver(
        user_id=user_id,
        ratings=5,
        state="free",
    )
    try:
        db.add(db_driver)
        db.commit()
        db.refresh(db_driver)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


def add_vehicle_to_db(vehicle: DriverVehicle, user_id: int, db: Session):
    db_vehicle = Vehicle(
        user_id=user_id,
        licence_plate=vehicle.licence_plate,
        model=vehicle.model,
    )
    try:
        create_driver(user_id, db)
        db.add(db_vehicle)
        db.commit()
        db.refresh(db_vehicle)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


def get_driver_profile(user_id: int, db: Session):
    return db.query(drivers_models.Driver).filter(drivers_models.Driver.user_id == user_id).first()


def get_driver_vehicle(user_id: int, db: Session):
    try:
        db_driver = db.query(drivers_models.Vehicle).filter(
            drivers_models.Vehicle.user_id == user_id).first()
        return db_driver
    except Exception as _:
        raise HTTPException(status_code=500, detail="Internal server error")


def get_available_drivers(db: Session):
    try:
        q = db.query(drivers_models.Driver).filter(
            drivers_models.Driver.state == "free").all()
        if not q:
            return []
        return list(q)
    except Exception as _:
        raise HTTPException(status_code=500, detail="Internal server error")


def update_driiver_profile_db(new_profile: DriverProfile, user_db, db: Session):
    old_driver = get_driver_profile(user_db.user_id, db)

    if not old_driver:
        raise HTTPException(status_code=404, detail="The driver doesn't exist")

    old_vehicle = get_driver_vehicle(user_db.user_id, db)
    if not old_vehicle:
        db_vehicle = Vehicle(
            user_id=user_db.user_id,
            licence_plate=new_profile.licence_plate,
            model=new_profile.model,
        )
        try:
            db.add(db_vehicle)
            db.commit()
            db.refresh(db_vehicle)
        except Exception:
            raise HTTPException(
                status_code=500, detail="Internal server error")

    try:
        if new_profile.username is not None:
            user_db.username = new_profile.username
        if new_profile.surname is not None:
            user_db.surname = new_profile.surname
        if new_profile.licence_plate is not None:
            old_vehicle.licence_plate = new_profile.licence_plate
        if new_profile.model is not None:
            old_vehicle.model = new_profile.model
        db.commit()
        return
    except Exception as _:
        raise HTTPException(status_code=500, detail="Internal server error")


def add_driver_rating(email, trip_id, rating, message, db: Session):
    db_rating = DriverRating(
        email=email,
        trip_id=trip_id,
        ratings=rating,
        message=message
    )
    try:
        db.add(db_rating)
        db.commit()
        db.refresh(db_rating)
    except Exception as _:
        raise HTTPException(status_code=500, detail="Internal server error")


def get_driver_average_ratings(email, db: Session):
    try:
        ratings = db.query(DriverRating).filter(DriverRating.email == email).all()
        sum = 0
        for rating in ratings:
            sum += rating.ratings
        if len(ratings) == 0:
            return 5
        return sum / len(ratings)
    except Exception as _:
        raise HTTPException(status_code=500, detail="Internal server error")


def get_all_driver_ratings(email, db: Session):
    try:
        ratings = db.query(DriverRating).filter(DriverRating.email == email).all()
        return ratings
    except Exception as _:
        raise HTTPException(status_code=500, detail="Internal server error")


def get_driver_ratings(ratings_id, db: Session):
    return db.query(DriverRating).filter(DriverRating.id == ratings_id).first()
