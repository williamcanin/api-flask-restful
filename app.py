import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from api import settings
from api.utils.database import db
from api.users.registers import init_app_users, resources_users


# Apps instance
users = settings.Base(init_app_users, resources_users)


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(settings.environment[environment])
    db.init_app(app)
    settings.Base(["api.utils.errors:init_app"], []).register(app)
    users.register(app)
    return app


app = create_app(os.getenv('FLASK_ENV'))
app.app_context().push()
migrate = Migrate(app, db)
CORS(app)
