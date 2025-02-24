"""Configuration file using environment variables."""

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


class Config:
    """
    Configuration class for Flask application.
    Pulls in configuration from environment variables (12-factor compliance).
    """

    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///weather.db")

    DEBUG = False
    TESTING = False
    # A secret key (needed for sessions in Flask, if used)
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")  # 'dev' as default for development

    # Weather API specific config:
    WEATHER_API_KEY = os.environ.get(
        "WEATHER_API_KEY"
    )  # No default; should be set in env
    WEATHER_API_URL = os.environ.get(
        "WEATHER_API_URL", "http://api.weatherapi.com/v1/current.json"
    )

    # TODO:
    # Other configs like database URL could be here as needed

    @staticmethod
    def dummy_method():
        """Pylint workaround for too-few-public-methods."""
        pass
