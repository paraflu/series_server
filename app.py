import argparse
from distutils.debug import DEBUG
import json
import logging
import sys
from api.parser import parser_api
from flask import Flask, abort, jsonify, request
from firebase_admin import auth
from imdbstore import IMDBStore, Serie as IMDBSerie

from wiki_parser.parser import WikiParser
from db import Db
from groups import groups_route

app = Flask(__name__)
app.debug = True

app.register_blueprint(parser_api)
app.register_blueprint(groups_route)


@app.route('/')
def index():
    return "ping"


def users():
    page = auth.list_users()
    while page:
        for user in page.users:
            yield user
        # Get next batch of users.
        page = page.get_next_page()

from datetime import date, datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

# @app.route('/users')
# def _users_():
#     return jsonify([{"uid": u.uid, "email": u.email, "display_name": u.display_name} for u in users()])

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='TvSeries Scraper')
    parser.add_argument('-c', '--cli', action='store_true')
    parser.add_argument('-i', '--imdb', nargs="+", type=int)
    parser.add_argument('url', nargs="*")

    args = parser.parse_args()

    if args.cli:
        import logging
        logging.basicConfig(level=logging.DEBUG)
        
        if args.imdb:
            for id in args.imdb:
                serie = IMDBSerie(id)
                print(json.dumps(serie.to_dict(), default=json_serial))
                sys.exit(0)

        if not args.url:
            sys.stderr.write(f'Parametro <url> non trovato')
            sys.exit(2)

        db = Db()
        # group_id = db.groups[0].id

        # user = next(users())
        # for g in db.groups:
        #     if user.uid in g.to_dict()['users']:
        #         guid = g.id
        #         break
        
        store = IMDBStore()

        for u in args.url:
            serie = WikiParser(u).get()
            #imdb_serie = store.searchById(72)
            # if not group_id in serie.groups:
            #     serie.groups.add(group_id)
            logging.debug(serie)
            r = db.add_serie(serie)
            logging.debug(r)
    else:
        app.run()
