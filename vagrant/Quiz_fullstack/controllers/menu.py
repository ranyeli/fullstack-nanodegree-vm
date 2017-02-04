from app import app
from flask import render_template


@app.route('/restaurant/<int:restaurant_id>/menu')
def restaurantMenu(restaurant_id):
    return render_template('menu.html')


@app.route('/restaurant/<int:restaurant_id>/menuitem/new')
def newMenu(restaurant_id):
    return render_template('newMenu.html')


@app.route('/restaurant/<int:restaurant_id>/menuitem/<int:item_id>/edit')
def editMenu(restaurant_id, item_id):
    return render_template('editMenu.html')


@app.route('/restaurant/<int:restaurant_id>/menuitem/<int:item_id>/delete')
def deleteMenu(restaurant_id, item_id):
    return render_template('deleteMenu.html')