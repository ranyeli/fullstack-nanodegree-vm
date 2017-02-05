from app import app
from flask import render_template, redirect, request, url_for
from services.menuservice import *
from services.restaurantservice import get_restaurant


@app.route('/restaurant/<int:restaurant_id>/menu')
def restaurantMenu(restaurant_id):
    menu = get_restaurant_menu(restaurant_id)
    restaurant = get_restaurant(restaurant_id)
    return render_template('menu.html', menu=menu, restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/menuitem/new')
def newMenu(restaurant_id):
    restaurant = get_restaurant(restaurant_id)
    courses = get_all_courses()
    return render_template('newMenu.html', restaurant=restaurant, courses=courses)


@app.route('/restaurant/<int:restaurant_id>/menuitem/new', methods=['POST'])
def newMenuPOST(restaurant_id):
    save_menu_item(request, restaurant_id)
    return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))


@app.route('/restaurant/<int:restaurant_id>/menuitem/<int:item_id>/edit')
def editMenu(restaurant_id, item_id):
    return render_template('editMenu.html')


@app.route('/restaurant/<int:restaurant_id>/menuitem/<int:item_id>/delete')
def deleteMenu(restaurant_id, item_id):
    return render_template('deleteMenu.html')