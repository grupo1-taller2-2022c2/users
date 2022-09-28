from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from app.cruds.users_cruds import get_user
from app.cruds.drivers_cruds import *
from app.schemas.drivers_schemas import *
from app.database import get_db

router = APIRouter()


@router.post("/vehicle", status_code=status.HTTP_200_OK)
def add_vehicle(vehicle: DriverVehicle, db: Session = Depends(get_db)):
    db_user = get_user(vehicle.email, db)
    if not db_user:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    return add_vehicle_to_db(vehicle, db_user.user_id, db)
