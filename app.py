import argparse
from distutils.debug import DEBUG
import logging
import sys
from api.parser import parser_api
from flask import Flask

from api.wiki_parser.parser import Parser
from db import Db

app = Flask(__name__)
app.debug = True

app.register_blueprint(parser_api, url_prefix="/api")


@app.route('/')
def index():
    return "index"


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='TvSeries Scraper')
    parser.add_argument('-c', '--cli', action='store_true')
    parser.add_argument('url', nargs="*")

    args = parser.parse_args()

    if args.cli:
        import logging
        logging.basicConfig(level=logging.DEBUG)

        if not args.url:
            sys.stderr.write(f'Parametro <url> non trovato')
            sys.exit(2)

        
        db = Db()
        for u in args.url:
            serie = Parser(u).get()
            logging.debug(serie)
            r = db.add_serie(serie)
            logging.debug(r)
    else:
        app.run()
