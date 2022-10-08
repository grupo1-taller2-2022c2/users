from app.models.drivers_models import Driver, Vehicle
from app.schemas.drivers_schemas import DriverVehicle
import app.models.drivers_models as drivers_models
from sqlalchemy.orm import Session
from fastapi import HTTPException


def create_driver(user_id: int, db: Session):
    db_driver = Driver(
        user_id=user_id,
        ratings=5,
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
        db_driver = db.query(drivers_models.Vehicle).filter(drivers_models.Vehicle.user_id == user_id).first()
        return db_driver
    except Exception as _:
        raise HTTPException(status_code=500, detail="Internal server error")
