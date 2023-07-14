from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        super().__init__(tire_wear)
        self.tire_need_to_service = 3

    def needs_service(self):
        return sum(self.tire_wear) >= self.tire_need_to_service
