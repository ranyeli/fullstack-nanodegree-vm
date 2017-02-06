import sys
sys.path.append('../')
from sqlalchemy import create_engine
from models.base import Base
import models.menuitem
import models.restaurant
import models.course


engine = create_engine('sqlite:///../dbs/restaurantmenu.db')
Base.metadata.create_all(engine)