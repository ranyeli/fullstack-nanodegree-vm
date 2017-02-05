from crud.restaurantcrud import *
from models.restaurant import Restaurant


def save_restaurant(request):
    restaurant = Restaurant(name=request.form['rest_name'])
    add_restaurant(restaurant)

def edit_restaurant(request, restaurant_id):
    restaurant = get_restaurant(restaurant_id)
    restaurant.name = request.form['rest_name']
    add_restaurant(restaurant)