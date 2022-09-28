from sqlalchemy import Column, Integer, String
from app.models import Base


class Passenger(Base):
    __tablename__ = 'passengers'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    ratings = Column(Integer, nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    street_name = Column(String(50), nullable=False)
    street_number = Column(Integer, nullable=False)
