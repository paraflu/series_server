from flask import Flask

from api import parser_api


app = Flask(__name__)
app.register_blueprint(parser_api, url_prefix="/api")


@app.route('/')
def index():
    return "index"