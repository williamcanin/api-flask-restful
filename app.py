import os
from flask import Flask
from api import settings
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from api import db
from api.controller.user import (
    Home,
    GetUser,
    AddUser,
    UserAll,
    DeleteUser,
    PutUser
)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(settings.config_by_name[config_name])
    db.init_app(app)
    settings.init_apps(app)

    return app


app = create_app(os.getenv('FLASK_ENV'))
app.app_context().push()
migrate = Migrate(app, db)
api = Api(app)
CORS(app)


# Routes
api.add_resource(Home, "/")
api.add_resource(UserAll, "/users/")
api.add_resource(GetUser, "/user/<string:username>/")
api.add_resource(AddUser, "/user/add/")
api.add_resource(DeleteUser, "/user/delete/<int:id>/")
api.add_resource(PutUser, "/user/change/<string:username>/")
