
import os
from firebase_admin import firestore, auth

from api.wiki_parser.serie import Serie


class Db:
    def __init__(self):
        self.db = firestore.client()

    def add_serie(self, serie: Serie, gid: str = None):
        item = self.db.collection('serie').document(serie.title)
        if gid is None:
            gid = self.default_group()
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

    @property
    def serie(self):
        itemRef = self.db.collection('serie')
        return itemRef.get()

    @property
    def groups(self):
        groupsRef = self.db.collection('groups')
        return groupsRef.get()

    @property
    def users():
        page = auth.list_users()
        while page:
            for user in page.users:
                yield user
            # Get next batch of users.
            page = page.get_next_page()

    def default_group(self) -> str:
        user = next(self.users)
        guid = None
        for g in self.groups:
            if user.uid in g.to_dict()['users']:
                guid = g.id
                break
        return guid
