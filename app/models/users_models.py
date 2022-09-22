from sqlalchemy import Column, Integer, String

from app.database import Base


class User(Base):
    # __table_args__ = {"schema": "users"}
    __tablename__ = 'users'
    # user_id = Column(Integer, autoincrement=True)
    email = Column(String(50), primary_key=True, nullable=False)
    password = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    email = Column(String(50), primary_key=True, nullable=False)
    street_name = Column(String(50), nullable=False)
    street_number = Column(Integer, nullable=False)
