from sqlalchemy import Column, Integer, String, Boolean
from app.models import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    blocked = Column(Boolean, nullable=False)
