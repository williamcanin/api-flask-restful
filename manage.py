import os
from flask import Flask
from app.main.settings import config_by_name
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from app.main.commands import createsuperuser
from app.main import db
from app.main.model.user import User
from app.main.controller.user import (
    Home,
    GetUser,
    UserPost,
    UserAll,
    DeleteUser,
    PutUser
)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    with app.app_context():

        @app.cli.command('createsuperuser')
        def run_createsuperuser():
            createsuperuser(User)

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
api.add_resource(UserPost, "/user/add/")
api.add_resource(DeleteUser, "/user/delete/<int:id>/")
api.add_resource(PutUser, "/user/change/<string:username>/")
