from crud.menucrud import *
from models.menuitem import MenuItem


def edit_menu_item(request, item_id):
    menuitem = get_menu_item(item_id)
    menuitem.price = request.form['item_price']
    menuitem.name = request.form['item_name']
    menuitem.course = request.form['item_course']
    menuitem.description = request.form['item_desc']
    add_menu_item(menuitem)


def save_menu_item(request, restaurant_id):
    menuitem = MenuItem()
    menuitem.price = request.form['item_price']
    menuitem.name = request.form['item_name']
    menuitem.course = request.form['item_course']
    menuitem.description = request.form['item_desc']
    menuitem.restaurant_id = restaurant_id
    add_menu_item(menuitem)


