
import base64
import json
import os
import firebase_admin
from firebase_admin import credentials

default_app = None
if default_app is None:
    if 'CRED_STORE' in os.environ:
        if os.path.isfile(os.environ['CRED_STORE']):
            data = json.load(os.environ["CRED_STORE"])
        else:
            data = json.loads(base64.b64decode(os.environ['CRED_STORE']))
        cred = credentials.Certificate(data)
        default_app = firebase_admin.initialize_app(cred)
    else:
        raise Exception("CRED_STORE not set")
