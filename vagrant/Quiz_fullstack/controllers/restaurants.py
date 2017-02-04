from app import app
from flask import render_template
from datetime import datetime

@app.route('/')
@app.route('/restaurants')
def restaurantHome():
    return render_template('restaurants.html', date=datetime.now().year)


@app.route('/restaurants/new')
def newRestaurant():
    return render_template('newRestaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return render_template('editRestaurant.html')


@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return render_template('deleteRestaurant.html')