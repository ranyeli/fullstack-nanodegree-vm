from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import relationship
from  sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    __tablename__ = 'restaurant'

class MenuItem(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    __tablename__ = 'menu_item'

    @property
    def serialize(self):
        return {
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'course': self.course,
            'id': self.id
        }

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)