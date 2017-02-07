from waitress import serve
from finalproject import app

app.secret_key = 'thisIsMySecretKey'


if __name__ == '__main__':

    app.debug = True
    serve(app, listen='*:80')

