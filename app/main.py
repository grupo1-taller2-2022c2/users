from fastapi import FastAPI
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users_routes, passengers_routes, drivers_routes
from starlette import status
from app.database import get_db
from sqlalchemy.orm import Session
from app.cruds import users_cruds, passengers_cruds, drivers_cruds

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Go sign in"}

app.include_router(users_routes.router, prefix="/users", tags=["users"])
app.include_router(passengers_routes.router,
                   prefix="/passengers", tags=["passengers"])
app.include_router(drivers_routes.router, prefix="/drivers", tags=["drivers"])


@app.delete("/reset_db", status_code=status.HTTP_200_OK)
def reset_database(db: Session = Depends(get_db)):
    users_cruds.delete_added_users(db)
    passengers_cruds.delete_added_passengers(db)
    drivers_cruds.delete_added_drivers(db)
    return "Successfully reset"
