from waitress import serve
from finalproject import app


serve(app, listen='*:8080')

