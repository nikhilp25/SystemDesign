from vehicle_size import VehicleSize
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, license_number,size):
        self.license_number = license_number
        self.size = size

        def get_license_number(self):
            return self.license_number

        def get_size(self):
            return self.size

class Bike(Vehicle):
    def __init__(self, license_number):
        super().__init__(license_number, VehicleSize.SMALL)

class Car(Vehicle):
    def __init__(self, license_number):
        super().__init__(license_number, VehicleSize.MEDIUM)

class Truck(Vehicle):
    def __init__(self, license_number):
        super().__init__(license_number, VehicleSize.LARGE)