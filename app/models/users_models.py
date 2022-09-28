from sqlalchemy import Column, Integer, String, Date

from app.models import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True)
    email = Column(String(50), primary_key=True, nullable=False)
    password = Column(String(50))
