# import os
# import unittest
# from unittest.mock import patch, MagicMock
# from weatherlib import provider

# class TestWeatherProvider(unittest.TestCase):
#     @patch('weatherlib.provider.requests.get')
#     def test_get_current_weather_success(self, mock_get):
#         # Setup the mock
#         fake_response = MagicMock()
#         fake_response.status_code = 200
#         fake_response.json.return_value = {"foo": "bar"}  # sample data
#         fake_response.raise_for_status = lambda: None  # do nothing
#         mock_get.return_value = fake_response

#         os.environ['WEATHER_API_KEY'] = 'testkey'
#         result = provider.get_current_weather("TestCity")
#         expected_url = provider.BASE_URL + f"?key=testkey&q=TestCity"
#         mock_get.assert_called_once_with(expected_url, timeout=5)
#         self.assertEqual(result, {"foo": "bar"})
