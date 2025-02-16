
import unittest
from weatherlib import utils

class TestWeatherUtils(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        # 0°C -> 32°F
        self.assertAlmostEqual(utils.celsius_to_fahrenheit(0), 32.0, places=1)
        # 100°C -> 212°F
        self.assertAlmostEqual(utils.celsius_to_fahrenheit(100), 212.0, places=1)
        # Negative values
        self.assertAlmostEqual(utils.celsius_to_fahrenheit(-40), -40.0, places=1)  # -40 is the same in both
