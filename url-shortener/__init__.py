from flask import Flask, request
from . import db


def create_app():
    app = Flask(__name__)
    db.client.init_db(app)

    @app.route('/', methods=['GET'])
    def get_all_codes():
        return "<p>Get Codes</p>"

    @app.route('/<string:short_url>', methods=['GET', 'POST'])
    def get_code(short_url):
        if request.method == 'GET':
            return "<p>Get Code</p>"
        else:
            return "<p>Create Code </p>"

    return app
