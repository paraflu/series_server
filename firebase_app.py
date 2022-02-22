
import os
import firebase_admin
from firebase_admin import credentials

default_app = None
if default_app is None:
    if 'CRED_STORE' in os.environ:
        cred = credentials.Certificate(os.environ['CRED_STORE'])
        default_app = firebase_admin.initialize_app(cred)
    else:
        raise Exception("CRED_STORE not set")
