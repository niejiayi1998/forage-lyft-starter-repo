from car import Car

from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine
from engine.engine_type.sternman_engine import SternmanEngine

from battery.battery_type.spindler_battery import SpindlerBattery
from battery.battery_type.nubbin_battery import NubbinBattery

from tire.tire_type.carrigan_tire import CarriganTire
from tire.tire_type.octoprime_tire import OctoprimeTire

class CarFactory:
    @staticmethod
    def create_callope(current_date, last_service_date,
                       current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date,
                        current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_palindrome(self, current_date, last_service_date,
                          warning_light_on, tire_wear):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_rorschach(self, current_date, last_service_date,
                         current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_thovex(self, current_date, last_service_date,
                      current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car
