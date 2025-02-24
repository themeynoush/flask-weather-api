import pytest
from app.models import SessionLocal, WeatherData
from app import create_app

@pytest.fixture
def client():
    """Set up a Flask test client."""
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_weather_caching(client, mocker):
    """Ensure API request is cached in the database."""
    session = SessionLocal()
    
    # Mock API response
    mock_data = {
        "city": "Paris",
        "temperature_c": 2000.0,
        "temperature_f": 6800.0,
        "condition": "Sunny",
    }
    
    # Insert weather data into DB
    session.add(WeatherData(**mock_data))
    session.commit()
    
    # Mock API call (should NOT be called)
    mock_get_weather = mocker.patch("weatherlib.provider.get_current_weather", return_value=mock_data)
    
    # First request (uses database cache)
    response = client.get("/weather/current?city=Paris")
    
    assert response.status_code == 200
    assert response.json["location"] == "Paris"
    
    # Ensure the API provider was **not** called
    mock_get_weather.assert_not_called()
    
    session.close()
