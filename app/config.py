""" Configuration file using environment variables. """

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv("WEATHER_API_KEY")


class Config:
    """
    Configuration class for Flask application.
    Pulls in configuration from environment variables (12-factor compliance).
    """

    DEBUG = False
    TESTING = False
    # Example: configure a secret key (needed for sessions in Flask, if used)
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")  # 'dev' as default for development

    # Weather API specific config:
    WEATHER_API_KEY = os.environ.get(
        "WEATHER_API_KEY"
    )  # No default; should be set in env
    WEATHER_API_URL = os.environ.get(
        "WEATHER_API_URL", "http://api.weatherapi.com/v1/current.json"
    )
    # Note: For Open-Meteo, you might use a different URL entirely

    # Other configs like database URL could be here as needed
