from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
# from app.database import Base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True)
    email = Column(String(50), primary_key=True, nullable=False)
    password = Column(String(50))
