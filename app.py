import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from api.parser import parser_api

dbfile = 'series.sqlite3'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dbfile}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
if not os.path.exists(dbfile):
    db.create_all()


app.register_blueprint(parser_api, url_prefix="/api")


@app.route('/')
def index():
    return "index"
