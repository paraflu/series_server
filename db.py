
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from api.wiki_parser.serie import Serie


class Db:
    def __init__(self, credential_file: str):
        self.cred = credentials.Certificate(credential_file)
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def add_serie(self, serie: Serie):
        item = self.db.collection('serie').document(serie.title)
        doc = item.get()
        if doc.exists:
            item.update(serie.to_dict())
        else:
            item.set(serie.to_dict())
        return doc

    def get(self, serie_name: str):
        return self.find(serie_name)

    def find(self, serie_name: str):
        itemRef = self.db.collection('serie').document(serie_name)
        return itemRef.get()

    @property
    def serie(self):
        itemRef = self.db.collection('serie')
        return itemRef.get()
    
