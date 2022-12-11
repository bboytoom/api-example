import os

from logging.config import dictConfig
from src.config.logger import config


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SERVER_NAME = os.environ.get('HOST')

    dictConfig(config)


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


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
