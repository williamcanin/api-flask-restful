import os
from importlib import import_module

basedir = os.path.abspath(os.path.dirname(__file__))


init_app_list = [
    "api.cli.user:init_app",
    "api.utils.errors:init_app",
]


def init_apps(app):
    for item in init_app_list:
        module_name, function = item.split(":")
        mod = import_module(module_name)
        getattr(mod, function)(app)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious_secret_key")
    DEBUG = False

# NOTE: Using "replace" for Heroku to recognize "postgresql://"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = {
    "development": DevelopmentConfig,
    "test": TestingConfig,
    "production": ProductionConfig,
}

key = Config.SECRET_KEY
