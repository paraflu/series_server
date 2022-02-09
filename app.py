import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

dbfile = 'series.sqlite3'

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dbfile}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
if not os.path.exists(dbfile):
    db.create_all()

migrate = Migrate(app, db)

from api.parser import parser_api
app.register_blueprint(parser_api, url_prefix="/api")


@app.route('/')
def index():
    return "index"


if __name__ == "__main__":
    app.run()
