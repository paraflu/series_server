from cmath import exp
import os
from pprint import pprint
from flask import Blueprint, abort, jsonify, request
from itsdangerous import json
from api.auth import validate_request
# from api.models.serie import Serie

from api.wiki_parser import Parser
from api.wiki_parser.serie import Serie
# from app import db
from db import Db
import logging

from firebase_app import init_app

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

parser_api = Blueprint('api', __name__)

init_app()

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
