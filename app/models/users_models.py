from sqlalchemy import Column, Integer, String, Date

from app.database import Base


class User(Base):
    __tablename__ = 'users'
    email = Column(String(50), primary_key=True, autoincrement=True, nullable=False)
    password = Column(String(50))
