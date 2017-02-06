import sys
sys.path.append('../')
from sqlalchemy import create_engine
from models.base import Base
import models.menuitem
import models.restaurant
import models.course


engine = create_engine('postgresql://postgres@localhost/restaurantmenu')
Base.metadata.create_all(engine)
