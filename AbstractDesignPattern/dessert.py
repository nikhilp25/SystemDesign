from abc import ABC, abstractmethod

class Dessert(ABC):
    @abstractmethod
    def prepare(self):
        pass 