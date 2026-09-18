
from TransportMode import TransportMode
class TransportService:

    def __init__(self,mode:TransportMode):
        self.mode=mode
    
    def setTransportMode(self,mode:TransportMode):
        self.mode=mode
    
    def getETA(self):
        self.mode.eta()
    
    def getDirection(self):
        self.mode.direction()
