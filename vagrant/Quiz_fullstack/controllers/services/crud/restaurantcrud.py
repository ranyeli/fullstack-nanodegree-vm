# import sys
# sys.path.append('../../..')
from session import session
from models.restaurant import Restaurant

def get_restaurant(restaurant_id):
    return session.query(Restaurant).filter(Restaurant.id == restaurant_id).one()

def get_all_restaurants():
    return session.query(Restaurant).order_by(Restaurant.name.asc()).all()

def add_restaurant(restaurant):
    session.add(restaurant)
    session.commit()

def delete_restaurant(restaurant_id):
    session.query(Restaurant).filter(Restaurant.id == restaurant_id).delete()
    session.commit()

# rest = get_restaurant(1)
# print rest.name