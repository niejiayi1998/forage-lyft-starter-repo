import unittest

from tire.tire_type.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear = [0.6, 0.9, 0.8, 0.7]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.5, 0.9, 0.8, 0.7]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())
