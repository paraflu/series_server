from cmath import exp
from flask import Blueprint, abort, jsonify, request
from api.models.serie import Serie

from api.wiki_parser import Parser
from app import db

parser_api = Blueprint('api', __name__)


@parser_api.route('/')
def index():
    return "no data"


@parser_api.route('/parse', methods=['POST'])
def parse_data():
    try:
        serie = request.form['series']
        serie = Parser(serie).get()

        it = Serie.convert(serie)
        db.session.add(it)
        db.session.commit()
        return jsonify(it.as_dict())
    except Exception as e:
        return abort(500, e)
