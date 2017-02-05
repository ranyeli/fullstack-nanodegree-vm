# import sys
# sys.path.append('../../..')
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base


# engine = create_engine('sqlite:///../../../dbs/restaurantmenu.db')
# engine = create_engine('sqlite:///../../dbs/restaurantmenu.db')
engine = create_engine('sqlite:///dbs/restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

