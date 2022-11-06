from sqlalchemy import Column, Integer, String, Float
from app.models import Base


class Passenger(Base):
    __tablename__ = 'passengers'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    ratings = Column(Float, nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    street_name = Column(String(50), nullable=False)
    street_number = Column(Integer, nullable=False)


class PassengerRating(Base):
    __tablename__ = 'passenger_ratings'
    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(50), nullable=False)
    trip_id = Column(Integer, nullable=False)
    ratings = Column(Integer, nullable=False)
    message = Column(String(50), nullable=False)
