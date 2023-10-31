from sqlalchemy import Column, Integer, String
from .db import Base
import uuid

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=True)
    accessToken = Column(String, default=uuid.uuid4(), nullable=True)