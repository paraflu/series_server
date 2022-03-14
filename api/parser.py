from sys import prefix
from flask import Blueprint, abort, jsonify, request
import imdb
from api.auth import validate_request
from imdbstore import IMDBStore

from wiki_parser import WikiParser, parser
from wiki_parser.serie import Serie
from db import Db
import logging

import firebase_app

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

parser_api = Blueprint('api', __name__, url_prefix="/api")

fb = Db()


# @parser_api.route('/series')
# def serie_list():
#     serie_name = request.args.get('serie_name')
#     if serie_name is None:
#         return abort(400, {'error': True, 'message': 'badrequest'})
#     logger.debug(f'serie richiesta {serie_name}')
#     r = fb.find(serie_name)
#     if r is None:
#         return abort(404, {'error': True, 'message': 'not found'})
#     logger.debug("a", r.to_dict())
#     return jsonify(r.to_dict()), 200


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
        serie = WikiParser(url).get()
        r = fb.add_serie(serie)
        return jsonify(r.to_dict()), 200
    except Exception as e:
        logger.exception("Inserimento e parse fallito")
        return abort(500, e)


@parser_api.route('/sync')
def refresh():
    ids = []
    group_id = fb.groups[0].id
    for s in fb.serie:
        serie = WikiParser(s.to_dict()['url']).get()
        fb.add_serie(serie)
        ids.append(serie.title)
    return jsonify(ids), 200


@parser_api.route('/get', methods=['GET'])
def get():
    serie_name = str(request.args.get('id'))
    r = fb.find(serie_name)
    if r is None:
        return abort(404, {'error': True, 'message': 'not found'})
    return jsonify(r.to_dict()), 200


@parser_api.get('/imdb')
def get_imdb():
    # store = IMDBStore()
    # the_serie = store.searchById(id)
    serie = WikiParser('https://it.wikipedia.org/wiki/9-1-1_(serie_televisiva)').get(parse_imdb=True)
    return jsonify(serie.to_dict()), 200