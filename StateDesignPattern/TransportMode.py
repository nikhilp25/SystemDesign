from abc import ABC, abstractmethod

class TransportMode(ABC):
    @abstractmethod
    def eta(self):
        pass

    @abstractmethod
    def direction(self):
        pass

    