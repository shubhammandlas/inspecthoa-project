from sqlalchemy import Column, Integer, String
from .db import Base

class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=True)