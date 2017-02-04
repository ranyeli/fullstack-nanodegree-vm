from base import Base
from sqlalchemy import String, Column, Integer

class Course(Base):
    __tablename__= 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False,unique=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }