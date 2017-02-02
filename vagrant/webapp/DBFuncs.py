from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from vagrant.webapp.database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

def get_all_restaurants():
    return session.query(Restaurant).order_by(Restaurant.name.asc()).all()

def create_restaurant(name):
    restaurant = Restaurant(name = name)
    session.add(restaurant)
    session.commit()

def get_restaurant(id):
    return session.query(Restaurant).filter_by(id = id).one()

def update_restaurant(id, new_name):
    rest = get_restaurant(id)
    rest.name = new_name
    session.add(rest)
    session.commit()

def delete_restaurant(id):
    session.query(Restaurant).filter(Restaurant.id == id).delete()
    session.commit()

def get_menu_items():
    return session.query(MenuItem).order_by(MenuItem.id.asc()).all()

#for r in get_all_restaurants():
#    print r.name

#print get_restaurant(5).name

#import re
#print re.search("hola(\d+)", "hola569").group(1)

#delete_restaurant(12)