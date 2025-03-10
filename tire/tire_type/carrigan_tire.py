from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear):
        super().__init__(tire_wear)
        self.tire_need_to_service = 0.9

    def needs_service(self):
        for tire in self.tire_wear:
            if tire >= self.tire_need_to_service:
                return True
        return False
