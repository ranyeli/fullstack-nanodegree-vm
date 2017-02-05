from session import session
from models.menuitem import MenuItem


def delete_menuitem(item_id):
    session.query(MenuItem).filter(MenuItem.id == item_id).delete()
    session.commit()


def delete_restaurant_menu(restaurant_id):
    session.query(MenuItem).filter(MenuItem.restaurant_id == restaurant_id).delete()
    session.commit()


def get_menuitem(item_id):
    return session.query(MenuItem).filter(MenuItem.id == item_id).one()


def get_restaurant_menu(restaurant_id):
    return session.query(MenuItem).order_by(MenuItem.name.asc())\
        .filter(MenuItem.restaurant_id == restaurant_id).all()


def add_menuitem(item):
    session.add(item)
    session.commit()

