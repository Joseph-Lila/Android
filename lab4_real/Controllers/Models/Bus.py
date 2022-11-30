class Bus:
    def __init__(self, fio, bus_number, route_number, brand,
                 creation_year, vehicle):
        self.fio = fio
        self.bus_number = bus_number
        self.route_number = route_number
        self.brand = brand
        self.creation_year = creation_year
        self.vehicle = vehicle

    def edit(self, elem):
        self.fio = elem.fio
        self.bus_number = elem.bus_number
        self.route_number = elem.route_number
        self.brand = elem.brand
        self.creation_year = elem.creation_year
        self.vehicle = elem.vehicle

    def as_dict(self):
        return {
            'fio': self.fio,
            'bus_number': self.bus_number,
            'route_number': self.route_number,
            'brand': self.brand,
            'creation_year': self.creation_year,
            'vehicle': self.vehicle
        }
