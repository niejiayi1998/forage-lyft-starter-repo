from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.years_to_be_service = 3

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + self.years_to_be_service)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False
