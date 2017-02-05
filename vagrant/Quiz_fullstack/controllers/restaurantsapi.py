from app import app
from flask import jsonify
from services.restaurantservice import *


@app.route('/restaurants/JSON')
def restaurantsJSON():
    restaurants = get_all_restaurants()
    return jsonify(Restaurants=[restaurant.serialize for restaurant in restaurants])

