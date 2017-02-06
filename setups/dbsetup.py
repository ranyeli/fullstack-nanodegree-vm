import sys
sys.path.append('../')
from sqlalchemy import create_engine
from models.base import Base
import models.menuitem
import models.restaurant
import models.course


engine = create_engine('postgres://wbdchxpdhwsviw:5a5e6f7070ff650e9620a3c00533167944d8b516f826b9effebdefab69207008@ec2-54-163-234-4.compute-1.amazonaws.com:5432/df0u3r9mjc3vbs')
Base.metadata.create_all(engine)
