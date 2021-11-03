import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from api import settings
from api.utils.database import db
from api.registers import registers


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(settings.environment[environment])
    db.init_app(app)
    settings.Register(app, data=registers)
    return app


app = create_app(os.getenv('FLASK_ENV'))
app.app_context().push()
Migrate(app, db)
CORS(app)
