
import os
from firebase_admin import firestore

from api.wiki_parser.serie import Serie


class Db:
    def __init__(self):
        self.db = firestore.client()

    def add_serie(self, serie: Serie, gid: str):
        item = self.db.collection('serie').document(serie.title)
        doc = item.get()
        if doc.exists:
            grps = doc.to_dict()['groups']
            if not gid in grps:
                grps.append(gid)
            payload = serie.to_dict()
            payload.update({'groups': grps})
            item.update(payload)
        else:
            payload = serie.to_dict()
            payload.update({'groups': [gid]})
            item.set(payload)
        return doc

    def get(self, serie_name: str):
        return self.find(serie_name)

    def find(self, serie_name: str):
        itemRef = self.db.collection('serie').document(serie_name)
        return itemRef.get()

    @ property
    def serie(self):
        itemRef = self.db.collection('serie')
        return itemRef.get()

    @ property
    def groups(self):
        groupsRef = self.db.collection('groups')
        return groupsRef.get()
