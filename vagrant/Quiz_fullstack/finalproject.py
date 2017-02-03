from controllers.app import app
from controllers import restaurants
from controllers import menu


if __name__ == '__main__':
    app.secret_key = '!@#$%^&*()_+`sdft'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)