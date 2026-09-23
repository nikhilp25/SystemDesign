from vehicle import Vehicle
from parking_strategy import ParkingStrategy
from fee_strategy import FeeStrategy
from parking_strategy import NearestFirstStrategy
from fee_strategy import FlatRateFeeStrategy
from parking_ticket import ParkingTicket
from parking_floor import ParkingFloor
from typing import List, Dict, Optional

class ParkingLot:
    _instance= None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        self.floors: List[ParkingFloor] = []
        self.active_tickets: Dict[str, ParkingTicket] = {}
        self.fee_strategy = FlatRateFeeStrategy()
        self.parking_strategy = NearestFirstStrategy()

    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot._instance = ParkingLot()
        return ParkingLot._instance

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def set_fee_strategy(self, fee_strategy: FeeStrategy):
        self.fee_strategy = fee_strategy
    
    def set_parking_strategy(self, parking_strategy: ParkingStrategy):
        self.parking_strategy = parking_strategy
    
    def park_vehicle(self, vehicle:Vehicle):
        spot = self.parking_strategy.findSpot(self.floors,vehicle)
        if spot is not None:
            spot.park_vehicle(vehicle)
            ticket = ParkingTicket(spot,vehicle)
            self.active_tickets[ticket.get_ticket_id()] = ticket
            return ticket
        else:
            raise Exception("Parking lot is full")

    def unpark_vehicle(self, ticket_id: str):
        if ticket_id not in self.active_tickets:
            raise Exception("Invalid ticket ID")
        ticket = self.active_tickets[ticket_id]
        ticket.set_exit_time()
        fee = self.fee_strategy.calculate_fee(ticket)
        ticket.get_spot().unpark_vehicle()
        del self.active_tickets[ticket_id]
        return fee