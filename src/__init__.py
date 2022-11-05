import os

from flask import Flask
from dotenv import load_dotenv

load_dotenv('.env')


def create_app():
    from src.config.application import config

    app = Flask(__name__)
    app.config. from_object(config[os.environ.get('ENV')])

    # Routes
    register_blueprints(app)

    return app


def register_blueprints(app):
    from src.routes.api import api

    app.register_blueprint(api)

    @app.errorhandler(404)
    def page_not_found(e):
        return {'result': 'Resource not found'}, 404

    @app.errorhandler(500)
    def server_error(e):
        return {'result': 'Server error'}, 500
