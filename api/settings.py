import os
from importlib import import_module
from flask_restful import Api


BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Base:
    def __init__(self, init_app_list: list, resources_list: list):
        self.init_app_list = init_app_list
        self.resources_list = resources_list

    def init_app(self, app):
        if self.init_app_list:
            for item in self.init_app_list:
                module_name, function = item.split(":")
                mod = import_module(module_name)
                getattr(mod, function)(app)

    def resources(self, app):
        if self.resources_list:
            for item in self.resources_list:
                # Split: module name, function, route
                m, f, r = item.split("|")
                set_mod = import_module(m)
                attr_mod = getattr(set_mod, f)
                api = Api(app)
                api.add_resource(attr_mod, r)

    def register(self, app):
        self.init_app(app)
        self.resources(app)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious_secret_key")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    # Using "replace" for Heroku to recognize "postgresql://"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # Using "replace" for Heroku to recognize "postgresql://"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


environment = {
    "development": DevelopmentConfig,
    "test": TestingConfig,
    "production": ProductionConfig,
}
