from api.parser import parser_api
from flask import Flask

app = Flask(__name__)
app.debug = True

app.register_blueprint(parser_api, url_prefix="/api")

@app.route('/')
def index():
    return "index"


if __name__ == "__main__":
    app.run()
