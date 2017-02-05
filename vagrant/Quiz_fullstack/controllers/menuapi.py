from app import app
from flask import jsonify
from services.menuservice import *


@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    menu = get_restaurant_menu(restaurant_id)
    return jsonify(MenuItem=[item.serialize for item in menu])


@app.route('/menuitem/<int:item_id>/JSON')
def menuItemJSON(item_id):
    menuitem = get_menu_item(item_id)
    return  jsonify(menuitem.serialize)

