"""Application factory and initialization for the Flask app."""

import os
import logging
from flask import Flask
from sqlalchemy.exc import DatabaseError
from app.weather_routes import weather_bp
from app.models import init_db
from app.config import Config


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


def create_app(test_config=None):
    """
    Flask application factory. Creates and configures the Flask app.
    If test_config is provided, it will be used instead of the real config.
    """
    app = Flask(__name__)

    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_object(Config)

    # Initialize the database
    with app.app_context():
        try:
            init_db()
        except DatabaseError as e:
            if "sqlite" in Config.DATABASE_URL:
                logger.error(
                    "Database corruption detected: %s. \
                    Recreating SQLite database.",
                    e,
                )
                os.remove("weather.db")
                init_db()
            else:
                raise

    app.register_blueprint(weather_bp)

    return app
