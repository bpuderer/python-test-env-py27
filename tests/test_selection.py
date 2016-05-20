"""Demo selecting tests with nose attribute selector plugin.


-a slow
-a \!slow
-a '!slow'
-a life=42
-a slow,tags=tag2
-a slow tags=tag2
-a tags=tag1,tags=tag3
-a tags=tag1 tags=tag3
http://nose.readthedocs.io/en/latest/plugins/attrib.html
"""

from framework.testbase import BaseTestCase


class TestCaseSelection(BaseTestCase):
    """Demo basics of using test environment."""

    def test_timeouts(self):
        """Demo test selection - test_timeouts."""
        self.assertTrue(1)
    test_timeouts.slow = True

    def test_weather_forecast(self):
        """Demo test selection - test_weather_forecast."""
        self.assertTrue(1)
    test_weather_forecast.slow = True

    def test_something1(self):
        """Demo test selection - test_something1."""
        self.assertTrue(1)
    test_something1.life = 41

    def test_something2(self):
        """Demo test selection - test_something2."""
        self.assertTrue(1)
    test_something2.life = 42

    def test_no_attr_tags(self):
        """Demo test selection - test_no_attr_tags."""
        self.assertTrue(1)

    def test_feature_scenario1(self):
        """Demo test selection - test_feature_scenario1."""
        self.assertTrue(1)
    test_feature_scenario1.tags = ['tag1']

    def test_feature_scenario2(self):
        """Demo test selection - test_feature_scenario2."""
        self.assertTrue(1)
    test_feature_scenario2.slow = True
    test_feature_scenario2.tags = ['tag2']

    def test_feature_scenario3(self):
        """Demo test selection - test_feature_scenario3."""
        self.assertTrue(1)
    test_feature_scenario3.tags = ['tag1', 'tag2']

    def test_feature_scenario4(self):
        """Demo test selection - test_feature_scenario4."""
        self.assertTrue(1)
    test_feature_scenario4.tags = ['tag1', 'tag3']
