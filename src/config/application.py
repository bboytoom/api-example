import os

from logging.config import dictConfig
from src.config.logger import CONFIG


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    dictConfig(CONFIG)


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SERVER_NAME = os.environ.get('HOST')


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


config = {
    'test': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
    }
