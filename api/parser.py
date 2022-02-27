from flask import Blueprint, abort, jsonify, request
from api.auth import validate_request

from api.wiki_parser import Parser, parser
from api.wiki_parser.serie import Serie
from db import Db
import logging

import firebase_app

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

parser_api = Blueprint('api', __name__)

fb = Db()


@parser_api.route('/series')
def serie_list():
    serie_name = request.args.get('serie_name')
    if serie_name is None:
        return abort(400, {'error': True, 'message': 'badrequest'})
    logger.debug(f'serie richiesta {serie_name}')
    r = fb.find(serie_name)
    if r is None:
        return abort(404, {'error': True, 'message': 'not found'})
    logger.debug("a", r.to_dict())
    return jsonify(r.to_dict()), 200


@parser_api.route('/list')
def get_serie():
    return jsonify([s.to_dict()['title'] for s in fb.serie])


@parser_api.route('/parse', methods=['POST'])
def parse_data():
    """Parse di un url per ottenere la serie tv

    Returns:
        dict: serie parsata
    """
    try:
        url = request.form['url']
        serie = Parser(url).get()
        r = fb.add_serie(serie)
        return jsonify(r.to_dict()), 200
    except Exception as e:
        logger.exception("Inserimento e parse fallito")
        return abort(500, e)


@parser_api.route('/sync')
def refresh():
    for s in fb.serie:
        serie = Parser(s.to_dict()['url']).get()
        fb.add_serie(serie)
