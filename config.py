"""Config file passed to app """
import os


class Config(object):
    "Base config class"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    "Production config class"
    pass


class DevelopmentConfig(Config):
    "Development config class"
    DEBUG = True


class TestingConfig(Config):
    "Testing config class"
    TESTING = True