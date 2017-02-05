from crud.menucrud import *
from models.menuitem import MenuItem

def edit_menuitem(request, item_id):
    menuitem = get_menuitem(item_id)
    menuitem.price = request.form['m_price']
    menuitem.name = request.form['m_name']
    menuitem.course = request.form['m_course']
    menuitem.description = request.form['m_desc']
    add_menuitem(menuitem)


