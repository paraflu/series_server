
import os
import firebase_admin

default_app = None
if default_app is None:
    if 'CRED_STORE' in os.environ:
        default_app = firebase_admin.initialize_app(os.environ['CRED_STORE'])
    else:
        raise Exception("CRED_STORE not set")
