from fastapi import APIRouter, Depends, HTTPException

from starlette import status

from app.cruds.passengers_cruds import *
from app.cruds.users_cruds import get_user_by_email
from app.schemas.passengers_schemas import *
from app.database import get_db

router = APIRouter()


@router.post("/address", status_code=status.HTTP_201_CREATED)
def user_add_pred_address(user: PassengerAddress, db: Session = Depends(get_db)):
    db_user = get_user_by_email(user.email, db)
    if not db_user:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    return add_pred_address(user, db_user.user_id, db)


@router.get("/{useremail}", response_model=PassengerProfile, status_code=status.HTTP_200_OK)
def get_user(useremail: str, db: Session = Depends(get_db)):
    user_db = get_user_by_email(useremail, db)
    if not user_db:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    passenger_db = get_passenger_profile(user_db.user_id, db)
    profile = {
        "username": user_db.username,
        "surname": user_db.surname,
        "ratings": passenger_db.ratings
    }
    return profile


@router.get("/me/{useremail}", response_model=PassengerSelfProfile, status_code=status.HTTP_200_OK)
def get_user(useremail: str, db: Session = Depends(get_db)):
    user_db = get_user_by_email(useremail, db)
    if not user_db:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    passenger_db = get_passenger_profile(user_db.user_id, db)
    profile = {
        "email": useremail,
        "username": user_db.username,
        "surname": user_db.surname,
        "ratings": passenger_db.ratings
    }
    return profile


@router.patch("/update/{useremail}", status_code=status.HTTP_200_OK)
def update_passenger_profile(useremail: str, user: PassengerProfile, db: Session = Depends(get_db)):
    user_db = get_user_by_email(useremail, db)
    if not user_db:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    return update_passenger_profile_db(user, user_db, db)
