from vehicle_size import VehicleSize
from collections import defaultdict
from parking_spot import ParkingSpot
from typing import Dict
class ParkingFloor:
    def __init__(self,floorNumber):
        self.floorNumber = floorNumber
        self.spot :Dict[str, ParkingSpot] = {}

    def add_spot(self,spot):
        self.spot[spot.get_spot_id()] = spot

    def find_available_spot(self,vehicle):
        available_spot = [
            spot for spot in self.spot.values()
            if not spot.is_occupied_spot() and spot.can_fit_vehicle(vehicle)
        ]
        if available_spot:
            available_spot.sort(key=lambda x:x.get_spot_size().value)
            return available_spot[0]
        return None
    
    def display_availability(self):
        print(f"Floor {self.floorNumber} availability:")
        available_count = defaultdict(int)

        for spot in self.spot.values():
            if not spot.is_occupied_spot():
                available_count[spot.get_spot_size()] += 1
        for size in VehicleSize:
            print(f"{size.value} spots: {available_count[size]}")