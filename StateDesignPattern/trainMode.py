from TransportMode import TransportMode

class TrainMode(TransportMode):
    def eta(self):
        print("ETA for train mode")

    def direction(self):
        print("Direction for train mode")