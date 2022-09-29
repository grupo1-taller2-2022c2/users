from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import authorization_routes, users_routes, passengers_routes, drivers_routes, authorization_routes

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

app.include_router(authorization_routes.router, tags=["auth"])
app.include_router(users_routes.router, prefix="/users", tags=["users"])
app.include_router(passengers_routes.router,
                   prefix="/passengers", tags=["passengers"])
app.include_router(drivers_routes.router, prefix="/drivers", tags=["drivers"])
