from waitress import serve
from finalproject import app


if __name__ == '__main__':
    app.secret_key = 'thisIsMySecretKey'
    app.debug = True
    serve(app, listen='*:80')

