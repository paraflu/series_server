
import os
import firebase_admin

default_app = None

def init_app():
    if default_app is None:
        default_app = firebase_admin.initialize_app(os.environ['CRED_STORE'])
    return default_app
