from app import app
from flask import render_template
from datetime import datetime

@app.route('/')
@app.route('/restaurants')
def restaurantHome():
    return render_template('restaurants.html', date=datetime.now().year)


@app.route('/restaurants/new')
def newRestaurant():
    return 'Add restaurant'


@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return 'Editing restaurant {id} '.format(id=restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return 'Deleting restaurant {id} '.format(id=restaurant_id)