from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database_setup import Base, Restaurant, MenuItem
import json

engine = create_engine('sqlite:///dbs/restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_menu_items():
    return session.query(MenuItem).order_by(MenuItem.id.asc()).all()

def get_restaurant(id):
    return session.query(Restaurant).filter_by(id = id).one()

def get_restaurant_menus(id):
    return session.query(MenuItem).filter(MenuItem.restaurant_id == id).order_by(MenuItem.name.asc()).all()

def save_menu_item(item):
    session.add(item)
    session.commit()

def get_menu_item(menu_id):
    return session.query(MenuItem).filter_by(id=menu_id).one()

def delete_menu(menu_id):
    session.query(MenuItem).filter(MenuItem.id == menu_id).delete()
    session.commit()

#menus = get_restaurant_menus(5)
#print json.dump()
#print json.dumps(menus, default=dumper, indent=2)