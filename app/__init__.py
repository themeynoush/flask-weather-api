"""Application factory and initialization for the Flask app."""

import os
from flask import Flask
from app.weather_routes import weather_bp
from app.models import init_db


def create_app(test_config=None):
    """
    Flask application factory. Creates and configures the Flask app.
    If test_config is provided, it will be used instead of the real config.
    """
    app = Flask(__name__)

    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_object("app.config.Config")

    # Initialize the database
    with app.app_context():
        init_db()

    app.register_blueprint(weather_bp)

    return app


def create_app(test_config=None):
    """
    Flask application factory. Creates and configures the Flask app.
    If test_config is provided, it will be used instead of the real config.
    """
    app = Flask(__name__)

    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_object("app.config.Config")

    app.register_blueprint(weather_bp)

    return app
