import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

db_url = os.environ['DATABASE_URL']
engine = create_engine(db_url)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

