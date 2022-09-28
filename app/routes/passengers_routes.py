from fastapi import APIRouter, Depends, HTTPException

from starlette import status

from app.cruds.users_cruds import get_user
from app.cruds.passengers_cruds import *
from app.schemas.passengers_schemas import *
from app.database import get_db

router = APIRouter()


@router.post("/address", status_code=status.HTTP_200_OK)
def user_add_pred_address(user: PassengerAddress, db: Session = Depends(get_db)):
    db_user = get_user(user.email, db)
    if not db_user:
        raise HTTPException(
            status_code=404, detail="The user doesn't exist")
    return add_pred_address(user, db_user.user_id, db)
