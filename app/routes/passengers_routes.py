from fastapi import APIRouter, Depends, HTTPException, File

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
    ratings = get_passenger_average_ratings(useremail, db)
    photo = user_db.photo
    if photo is None:
        photo = "https://firebasestorage.googleapis.com/v0/b/fiuber-365100.appspot.com/o/user.jpg?alt=media&token=2f59f69b-124a-4431-9091-48ea98d57c25"
    profile = {
        "username": user_db.username,
        "surname": user_db.surname,
        "ratings": ratings,
        "photo": photo
    }
    return profile


@router.get("/me/{useremail}", response_model=PassengerSelfProfile, status_code=status.HTTP_200_OK)
def get_user(useremail: str, db: Session = Depends(get_db)):
    user_db = get_user_by_email(useremail, db)
    if not user_db:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    passenger_db = get_passenger_profile(user_db.user_id, db)
    ratings = get_passenger_average_ratings(useremail, db)
    photo = user_db.photo
    if photo is None:
        photo = "https://firebasestorage.googleapis.com/v0/b/fiuber-365100.appspot.com/o/user.jpg?alt=media&token=2f59f69b-124a-4431-9091-48ea98d57c25"
    profile = {
        "email": useremail,
        "username": user_db.username,
        "surname": user_db.surname,
        "ratings": ratings,
        "photo": photo
    }
    return profile


@router.patch("/{useremail}", status_code=status.HTTP_200_OK)
def update_passenger_profile(useremail: str, user: PassengerProfile, db: Session = Depends(get_db)):
    user_db = get_user_by_email(useremail, db)
    if not user_db:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    return update_passenger_profile_db(user, user_db, db)


@router.post("/ratings", status_code=status.HTTP_201_CREATED)
def user_add_passenger_ratings(rating: PassengerRating, db: Session = Depends(get_db)):
    """Add a rating to the passenger"""
    db_user = get_user_by_email(rating.passenger_email, db)
    if not db_user:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    return add_passenger_rating(rating.passenger_email, rating.trip_id, rating.ratings, rating.message, db)


@router.get("/ratings/all/{useremail}", status_code=status.HTTP_200_OK)
def user_get_passenger_ratings(useremail: str, db: Session = Depends(get_db)):
    db_user = get_user_by_email(useremail, db)
    if not db_user:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    return get_all_passenger_ratings(useremail, db)


@router.get("/ratings/{ratings_id}", status_code=status.HTTP_200_OK)
def user_get_passenger_rating(ratings_id: int, db: Session = Depends(get_db)):
    return get_passenger_ratings(ratings_id, db)
