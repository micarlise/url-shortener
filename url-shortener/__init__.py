from flask import Flask
from . import db
from . import urls


def create_app():
    app = Flask(__name__)
    db.client.init_db(app)

    app.register_blueprint(urls.bp)

    return app
