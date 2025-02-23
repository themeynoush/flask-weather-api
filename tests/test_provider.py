
import unittest
import weatherlib.utils as wu

# Simulate a sample response from the Weather API.
sample_api_response = {
    "location": {"name": "Paris"},
    "current": {
        "temp_c": 20.0,
        "condition": {"text": "Partly cloudy"}
    }
}

class TestWeatherProcessing(unittest.TestCase):
    def test_process_weather_data(self):
        result = wu.process_weather_data(sample_api_response)
        # Check that required keys are present
        self.assertIn("location", result)
        self.assertIn("temperature_c", result)
        self.assertIn("temperature_f", result)
        self.assertIn("condition", result)
        # Check values correctness
        self.assertEqual(result["location"], "Paris")
        self.assertEqual(result["temperature_c"], 20.0)
        self.assertAlmostEqual(result["temperature_f"], 68.0, places=1)  # 20C ~ 68F
        self.assertEqual(result["condition"], "Partly cloudy")
    
    def test_process_weather_data_empty(self):
        # If data is empty or None, should return empty dict without error
        self.assertEqual(wu.process_weather_data(None), {})
        self.assertEqual(wu.process_weather_data({}), {})
