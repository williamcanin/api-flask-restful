import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from api.utils.database import db
from api import settings


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(settings.config_by_name[config_name])
    db.init_app(app)
    settings.Base().init_apps(app)

    return app


app = create_app(os.getenv('FLASK_ENV'))
app.app_context().push()
migrate = Migrate(app, db)
CORS(app)
settings.Base().resources_import(app)
