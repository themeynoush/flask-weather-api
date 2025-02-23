def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def process_weather_data(data: dict) -> dict:
    """
    Process raw weather data from the provider into a simplified format.
    Extract location and curerent temperature in C and F certain fields and add conversions.
    """
    if not data:
        return {}
    processed = {}
    if "location" in data and "name" in data["location"]:
        processed["location"] = data["location"]["name"]
    if "current" in data:
        current = data["current"]
        if "temp_c" in current:
            temp_c = current["temp_c"]
            processed["temperature_c"] = temp_c
            processed["temperature_f"] = round(celsius_to_fahrenheit(temp_c), 2)
        if "condition" in current and "text" in current["condition"]:
            processed["condition"] = current["condition"]["text"]
    return processed
