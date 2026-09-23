from vehicle_size import VehicleSize
from vehicle import Vehicle
class ParkingSpot:
    def __init__(self,spot_id,spot_size):
        self.spot_id = spot_id
        self.spot_size = spot_size
        self.is_occupied = False
        self.parked_vehicle = None
    
    def get_spot_id(self):
        return self.spot_id
    
    def get_spot_size(self):
        return self.spot_size
    
    def is_available(self):
        return not self.is_occupied
    
    def is_occupied_spot(self):
        return self.is_occupied
    
    def park_vehicle(self,vehicle):
        self.is_occupied = True
        self.parked_vehicle = vehicle

    def unpark_vehicle(self):
        self.is_occupied = False
        self.parked_vehicle = None
    
    def can_fit_vehicle(self, vehicle):
        if self.is_occupied:
            return False
        
        if vehicle.size == VehicleSize.SMALL:
            return self.spot_size == VehicleSize.SMALL
        elif vehicle.size == VehicleSize.MEDIUM:
            return self.spot_size in [VehicleSize.SMALL, VehicleSize.MEDIUM]
        elif vehicle.size == VehicleSize.LARGE:
            return self.spot_size == VehicleSize.LARGE
        return False