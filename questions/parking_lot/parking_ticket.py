import time
import uuid

class ParkingTicket:
    def __init__(self,spot,vehicle):
        self.spot = spot
        self.tickerId = str(uuid.uuid4())
        self.vehicle = vehicle
        self.entry_time = int(time.time()*1000)
        self.exit_time = 0

    def get_ticket_id(self):
        return self.tickerId
    
    def get_spot(self):
        return self.spot
    
    def get_vehicle(self):
        return self.vehicle
    
    def set_exit_time(self):
        self.exit_time = int(time.time()*1000)

    def get_entry_time(self):
        return self.entry_time
    
    def get_exit_time(self):
        return self.exit_time
    
    def get_total_time(self):
        return self.exit_time - self.entry_time        