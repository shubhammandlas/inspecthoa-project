from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from .db import Base

class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True)
    fileName = Column(String(100))
    createdAt = Column(DateTime)
