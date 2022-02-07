from cmath import exp
from flask import Blueprint, abort, jsonify, request

from api.wiki_parser.episodes import Episodes

parser_api = Blueprint('api', __name__)


@parser_api.route('/')
def index():
    return "no data"


@parser_api.route('/parse', methods=['POST'])
def parse_data():
    try:
        serie = request.form['series']
        serie = Episodes(serie).get()
        return jsonify(serie.to_dict())
    except Exception as e:
        return abort(500, e)
