import os
import requests
from dotenv import load_dotenv

load_dotenv()  


API_KEY = os.environ.get('WEATHER_API_KEY')
BASE_URL = os.environ.get('WEATHER_API_URL', 'http://api.weatherapi.com/v1/current.json')

def get_current_weather(city: str) -> dict:
    """
    Fetch current weather data for the given city from WeatherAPI.
    Returns the parsed JSON as a Python dict.
    """
    if not API_KEY:
        raise RuntimeError("WEATHER_API_KEY not set in environment")
    url = f"{BASE_URL}?key={API_KEY}&q={city}"
    
    response = requests.get(url, timeout=5)
    response.raise_for_status()  
    
    data = response.json()  
    return data
