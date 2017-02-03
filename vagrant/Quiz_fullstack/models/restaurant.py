from sqlalchemy import Column, Integer, String
from base import Base


class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)