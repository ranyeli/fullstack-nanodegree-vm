import sys
import os
sys.path.append('../')
from sqlalchemy import create_engine
from models.base import Base
import models.menuitem
import models.restaurant
import models.course

db_url = os.environ['DATABASE_URL']
engine = create_engine(db_url)
Base.metadata.create_all(engine)
