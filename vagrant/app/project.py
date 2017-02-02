from flask import Flask, render_template, url_for, redirect, request, flash, jsonify, json
from dbfuncs import *
from config.database_setup import MenuItem

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def Hello():
    return 'Hello World'

@app.route('/menuitems')
def Menus():
    menus = get_menu_items()
    output = ""
    for item in menus: output += "<p>{i}<br/>{j}<br/>{z}</p>".format(i=item.name, j=item.price, z=item.description)
    return output

@app.route('/restaurant/<int:restaurant_id>')
def getRestaurant(restaurant_id):
    rest = get_restaurant(restaurant_id)
    menus = get_restaurant_menus(restaurant_id)
    return  render_template('menu.html', menus=menus, restaurant=rest)

@app.route('/restaurant/<int:restaurant_id>/newmenu', methods=['POST', 'GET'])
def newMenuItem(restaurant_id):
    if request.method == 'GET':
        rest = get_restaurant(restaurant_id)
        return render_template('newmenu.html', rest=rest)
    else:
        name = request.form['menu_name']
        desc = request.form['desc']
        price = request.form['price']
        course = request.form['course']
        newItem = MenuItem(name=name, description=desc, price=price, course=course, restaurant_id=restaurant_id)
        save_menu_item(newItem)
        return redirect(url_for('getRestaurant',restaurant_id=restaurant_id))

@app.route('/restaurant/<int:restaurant_id>/editmenu/<int:menu_id>', methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    menu = get_menu_item(menu_id)
    if request.method == 'GET':
        return render_template('editmenu.html', menu=menu, rest = restaurant_id)
    else:
        menu.name = request.form['menu_name']
        menu.description = request.form['desc']
        menu.price = request.form['price']
        menu.course = request.form['course']
        save_menu_item(menu)
        flash('menu %s has been edited' % menu.name)
        return redirect(url_for('getRestaurant',restaurant_id=restaurant_id))

@app.route('/restaurant/<int:restaurant_id>/deletemenu/<int:menu_id>', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    if(request.method == 'POST'):
        delete_menu(menu_id)
        flash('Menu has been deleted')
        return redirect(url_for('getRestaurant', restaurant_id=restaurant_id))
    else:
        menu = get_menu_item(menu_id)
        return render_template('deletemenu.html', menu=menu)

@app.route('/restaurant/<int:restaurant_id>/menus/json')
def restaurantMenuJSON(restaurant_id):
    menus = get_restaurant_menus(restaurant_id)
    return jsonify(MenuItem=[menu.serialize for menu in menus])

@app.route('/menu/<int:menu_id>/JSON')
def menuItemJSON(menu_id):
    menu = get_menu_item(menu_id)
    return jsonify(menu.serialize)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)