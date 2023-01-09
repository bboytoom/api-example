import os

from logging.config import dictConfig
from src.config.logger import CONFIG


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JSON_SORT_KEYS = False

    dictConfig(CONFIG)


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


config = {
    'test': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
    }
