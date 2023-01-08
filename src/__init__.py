import os


from dotenv import load_dotenv
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

load_dotenv('.env')

marshmallow = Marshmallow()
migrate = Migrate()


def create_app():
    from src.config.application import config
    from src.config.sqlalchemy_db import db
    from src.routes.api import api
    from src.routes.web import web

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[os.environ.get('ENV')])

    limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=['60/minute'])

    limiter.init_app(app)

    # Database
    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)

    # Routes
    app.register_blueprint(api)
    app.register_blueprint(web)
    register_error(app)

    return app


def register_error(app):
    from src.routes.errors import page_not_found, \
        internal_server_error, \
        rate_limit_handler, \
        bad_request_handler, \
        method_not_allow_handler, \
        unprocessable_entity

    app.register_error_handler(400, bad_request_handler)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, method_not_allow_handler)
    app.register_error_handler(422, unprocessable_entity)
    app.register_error_handler(429, rate_limit_handler)
    app.register_error_handler(500, internal_server_error)
