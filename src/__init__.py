import os

from flask import Flask
from dotenv import load_dotenv

load_dotenv('.env')


def create_app():
    from src.config.application import config

    app = Flask(__name__, instance_relative_config=True)
    app.config. from_object(config[os.environ.get('ENV')])

    # Routes
    register_blueprints(app)
    register_error(app)

    return app


def register_blueprints(app):
    from src.routes.api import api

    app.register_blueprint(api)


def register_error(app):
    from src.routes.errors import page_not_found, \
        internal_server_error

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
