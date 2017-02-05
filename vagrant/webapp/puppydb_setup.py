from sqlalchemy import create_engine
from  sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer, String, Date, Numeric, Column


PuppyBase = declarative_base()


class Shelter(PuppyBase):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(80), nullable=False)
    city = Column(String(20), nullable=False)
    state = Column(String(20), nullable=False)
    zipCode = Column(String(12), nullable=False)
    website = Column(String, nullable=True)


class Puppy(PuppyBase):
    __tablename__ = 'puppy'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    dateOfBirth = Column(Date, nullable=True)
    picture = Column(String, nullable=True)
    gender = Column(String(10), nullable=True)
    weight = Column(Numeric(10), nullable=True)
    shelter_id = Column(ForeignKey('shelter.id'))
    shelter = relationship(Shelter)

engine = create_engine('sqlite:///puppies.db')
PuppyBase.metadata.create_all(engine)

