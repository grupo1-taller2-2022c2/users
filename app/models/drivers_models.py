from sqlalchemy import Column, Integer, String, Float
from app.models import Base


class Driver(Base):
    __tablename__ = "drivers"
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    ratings = Column(Float, nullable=False)
    state = Column(String[50], nullable=False)


class Vehicle(Base):
    __tablename__ = "vehicles"
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    licence_plate = Column(String[50], nullable=False)
    model = Column(String[50], nullable=False)


class DriverRating(Base):
    __tablename__ = "driver_ratings"
    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(50), nullable=False)
    trip_id = Column(Integer, nullable=False)
    ratings = Column(Integer, nullable=False)
    message = Column(String(50), nullable=False)


class DriverReportModel(Base):
    __tablename__ = "driver_reports"
    id = Column(Integer, autoincrement=True, primary_key=True)
    driver_email = Column(String(50), nullable=False)
    passenger_email = Column(String(50), nullable=False)
    reason = Column(String(150), nullable=False)
    trip_id = Column(Integer, nullable=False)
