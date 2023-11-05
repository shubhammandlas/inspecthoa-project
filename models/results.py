from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from .db import Base

class Results(Base):
    __tablename__ = 'responses'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    requestId = Column(Integer, index=True)
    result = Column(Integer, nullable=False)