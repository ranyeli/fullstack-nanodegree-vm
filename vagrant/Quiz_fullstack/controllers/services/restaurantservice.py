# import sys
# sys.path.append('../..')
from sqlalchemy.orm.exc import NoResultFound
from crud.restaurantcrud import *
from models.restaurant import Restaurant


def save_restaurant(request):
    restaurant = Restaurant(name=request.form['rest_name'])
    add_restaurant(restaurant)