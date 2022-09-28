from app.models.drivers_models import Driver, Vehicle
from app.schemas.drivers_schemas import DriverVehicle
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
        licence_model=vehicle.licence_plate,
        model=vehicle.model,
    )
    try:
        db.add(db_vehicle)
        db.commit()
        db.refresh(db_vehicle)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
