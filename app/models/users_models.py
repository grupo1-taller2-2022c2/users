from sqlalchemy import Column, Integer, String, Date

from app.database import Base


class User(Base):
    # __table_args__ = {"schema": "users"}
    __tablename__ = 'users'
    # user_id = Column(Integer, autoincrement=True)
    email = Column(String(50), primary_key=True, nullable=False)
    password = Column(String(50), nullable=False)
