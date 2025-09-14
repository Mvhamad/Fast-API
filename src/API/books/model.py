from db import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, func

class Book(Base):
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    year = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    createdAt = Column(TIMESTAMP(timezone=True), default=func.now(), nullable=False)
    updatedAt = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now(), nullable=False)