from vehicle_size import VehicleSize
from abc import ABC, abstractmethod
from typing import List
from parking_floor import ParkingFloor
from vehicle import Vehicle
class ParkingStrategy(ABC):
    @abstractmethod
    def findSpot(self, floors:List[ParkingFloor],vehicle:Vehicle):
        pass

class NearestFirstStrategy(ParkingStrategy):
    def findSpot(self, floors:List[ParkingFloor],vehicle:Vehicle):
        for floor in floors:
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot
        return None

class FarthestFirstStrategy(ParkingStrategy):
    def findSpot(self, floors:List[ParkingFloor],vehicle:Vehicle):
        reversed_floors = list(reversed(floors))
        for floor in reversed_floors:
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot
        return None

class BestFitStrategy(ParkingStrategy):
    def findSpot(self, floors: List[ParkingFloor], vehicle: Vehicle):
        best_spot = None

        for floor in floors:
            spot_on_this_floor = floor.find_available_spot(vehicle)

            if spot_on_this_floor is not None:
                if best_spot is None:
                    best_spot = spot_on_this_floor
                else:
                    # A smaller spot size enum ordinal means a tighter fit
                    if list(VehicleSize).index(spot_on_this_floor.get_spot_size()) < list(VehicleSize).index(best_spot.get_spot_size()):
                        best_spot = spot_on_this_floor

        return best_spot
    