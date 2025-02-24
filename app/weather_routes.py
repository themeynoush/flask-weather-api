"""Define a Blueprint for weather-related routes."""

from flask import Blueprint, request, jsonify, current_app
from weatherlib import provider, utils
from app.models import SessionLocal, WeatherData

weather_bp = Blueprint("weather", __name__, url_prefix="/weather")


@weather_bp.route("/current", methods=["GET"])
def get_current_weather():
    """
    GET /weather/current?city=<CITY_NAME>
    Returns current weather data for the specified city as JSON.
    Expects a 'city' query parameter.
    """
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Missing required 'city' parameter"}), 400

    session = SessionLocal()

    # Check for cached weather data
    cached_weather = session.query(WeatherData).filter(WeatherData.city == city).first()
    if cached_weather:
        session.close()
        return jsonify(
            {
                "location": cached_weather.city,
                "temperature_c": cached_weather.temperature_c,
                "temperature_f": cached_weather.temperature_f,
                "condition": cached_weather.condition,
                "cached": True,
            }
        )

    # Fetch new weather data
    try:
        data = provider.get_current_weather(city)
    except ValueError as e:
        current_app.logger.exception("Weather data fetch failed")
        return (
            jsonify({"error": "Failed to fetch weather data", "details": str(e)}),
            500,
        )

    # Post-process the data
    processed = utils.process_weather_data(data)

    # Store the weather data in the database
    session = SessionLocal()

    try:
        weather_entry = WeatherData(
            city=processed["location"],
            temperature_c=processed["temperature_c"],
            temperature_f=processed["temperature_f"],
            condition=processed["condition"],
        )
        session.add(weather_entry)

        # Log the request
        log_entry = WeatherRequestLog(city=city)
        session.add(log_entry)

        session.commit()
    except Exception as e:
        session.rollback()
        current_app.logger.exception("Database insertion failed")
        return (
            jsonify({"error": "Failed to store weather data", "details": str(e)}),
            500,
        )
    finally:
        session.close()

    return jsonify(processed)
