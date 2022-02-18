from cmath import exp
import os
from flask import Blueprint, abort, jsonify, request
# from api.models.serie import Serie

from api.wiki_parser import Parser
from api.wiki_parser.serie import Serie
# from app import db
from db import Db
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

parser_api = Blueprint('api', __name__)


@parser_api.route('/')
def index():
    return "no data"


@parser_api.route('/parse', methods=['POST'])
def parse_data():
    try:
        serie = request.form['series']
        serie = Parser(serie).get()

        fb = Db(os.environ['CRED_STORE'])
        r = fb.add_serie(serie)
        # db.session.add(it)
        # db.session.commit()
        return jsonify(r)
    except Exception as e:
        logger.exception("Inserimento e parse fallito")
        return abort(500, e)
