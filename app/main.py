from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine

from .routes import users_routes


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Go sign in"}

Base.metadata.create_all(bind=engine)

app.include_router(users_routes.router, prefix="/users", tags=["users"])
