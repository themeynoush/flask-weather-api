""" Application factory and initialization for the Flask app. """
import os
from flask import Flask


def create_app(test_config=None):
    """
    Flask application factory. Creates and configures the Flask app.
    If test_config is provided, it will be used instead of the real config.
    """
    app = Flask(__name__)

    # Load configuration from environment or testing overrides
    if test_config:
        # In testing, use the provided configuration
        app.config.from_mapping(test_config)
    else:
        # Normal configuration
        # Example: ensure an important config like SECRET_KEY or others
        app.config.from_object("app.config.Config")

    # Register blueprints (in this case, we have a weather blueprint)
    from app.weather_routes import weather_bp

    app.register_blueprint(weather_bp)

    # Optionally, set up other aspects like error handlers here

    return app
