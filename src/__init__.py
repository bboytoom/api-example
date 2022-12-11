import os


from dotenv import load_dotenv
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv('.env')


def create_app():
    from src.config.application import config
    from src.routes.api import api

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[os.environ.get('ENV')])

    limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=['60/minute'])

    limiter.init_app(app)

    # Routes
    app.register_blueprint(api)
    register_error(app)

    return app


def register_error(app):
    from src.routes.errors import page_not_found, \
        internal_server_error, \
        ratelimit_handler

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(429, ratelimit_handler)
