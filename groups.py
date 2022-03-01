from flask import Blueprint, jsonify
from db import Db

groups_route = Blueprint('groups', __name__, url_prefix='/api/groups')

fb = Db()

@groups_route.route('/')
def list():
    return jsonify([g.to_dict() for g in fb.groups])



