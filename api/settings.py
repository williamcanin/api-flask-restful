import os
from importlib import import_module
from flask_restful import Api

# BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Base:
    def __init__(self):
        self.init_app_list = [
            "api.cli.user:init_app",
            "api.utils.errors:init_app",
        ]
        self.resources_list = [
            "api.controller.user|Home|/",
            "api.controller.user|GetUser|/user/<string:username>/",
            "api.controller.user|UserAll|/users/",
            "api.controller.user|AddUser|/user/add/",
            "api.controller.user|DeleteUser|/user/delete/<int:id>/",
            "api.controller.user|PutUser|/user/change/<string:username>/",
        ]

    def init_apps(self, app):
        for item in self.init_app_list:
            module_name, function = item.split(":")
            mod = import_module(module_name)
            getattr(mod, function)(app)

    def resources_import(self, app):
        for item in self.resources_list:
            m, f, r = item.split("|")
            mod = import_module(m)
            attr = getattr(mod, f)
            api = Api(app)
            api.add_resource(attr, r)


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
