
#https://makedeveasy.medium.com/authenitcation-using-python-flask-and-firestore-1958d29e2240

from functools import wraps
from flask import abort, request, session

from firebase_admin import auth

def validate_request(req_type):
    if req_type == 'json' and not request.json:
        abort(400)
    
    if 'Authentication' in request.headers:
        id_token = request.headers['Authentication']
        decoded_token = auth.verify_id_token(id_token)
        if 'uid' in decoded_token:
            session['uid'] = decoded_token['uid']
        else:
            abort(403)
    else:
        abort(403)
        
    def decorator(func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapped_func
    return decorator