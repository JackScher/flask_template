import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from .logger import log
from .database import db
from .routes import test_blueprint


def create_app() -> Flask:
    load_dotenv()

    app = Flask(__name__)
    log(log.INFO, "App initialized: [%s]", app.__class__.__name__)

    # Database.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints.
    app.register_blueprint(test_blueprint)

    return app

