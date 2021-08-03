from flask import Flask
from . import db
from . import urls


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config:
        app.config.from_mapping(test_config)

    # set up application
    db.client.init_db(app)
    app.register_blueprint(urls.bp)

    return app
