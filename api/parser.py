from flask import Blueprint, request

parser_api = Blueprint('api', __name__)


@parser_api.route('/')
def index():
    return "no data"


@parser_api.route('/parse', method='POST')
def parse_data():
    serie = request.form['series']
    return serie
