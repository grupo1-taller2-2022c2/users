from sqlalchemy import Column, Integer, String
from app.models import Base


class Driver(Base):
    __tablename__ = 'drivers'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    ratings = Column(Integer, nullable=False)
    state = Column(String[50], nullable=False)


class Vehicle(Base):
    __tablename__ = 'vehicles'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    licence_plate = Column(String[50], nullable=False)
    model = Column(String[50], nullable=False)
