from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base


engine = create_engine('postgresql://postgres@localhost:5432/restaurantmenu')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

