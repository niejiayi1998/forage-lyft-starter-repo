import unittest

from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.sternman_engine import SternmanEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 20000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 50000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 9999
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 50000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
