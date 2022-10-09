from app.models.passengers_models import Address, Passenger
from app.schemas.passengers_schemas import PassengerAddress
import app.models.passengers_models as passengers_models
from sqlalchemy.orm import Session
from fastapi import HTTPException


def create_passenger(user_id: int, db: Session):
    db_passenger = Passenger(
        user_id=user_id,
        ratings=5,
    )
    try:
        db.add(db_passenger)
        db.commit()
        db.refresh(db_passenger)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


def add_pred_address(address: PassengerAddress, user_id: int, db: Session):
    db_address = Address(
        user_id=user_id,
        street_name=address.street_name,
        street_number=address.street_number,
    )
    try:
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


def get_passenger_profile(user_id: int, db: Session):
    try:
        db_passenger = db.query(passengers_models.Passenger).filter(passengers_models.Passenger.user_id == user_id).first()
        return db_passenger
    except Exception as _:
        raise HTTPException(status_code=500, detail="Internal server error")
