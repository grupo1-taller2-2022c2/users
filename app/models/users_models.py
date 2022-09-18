from sqlalchemy import Column, Integer, String, Date

from app.database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
