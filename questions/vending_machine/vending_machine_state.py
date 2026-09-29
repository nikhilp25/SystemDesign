from abc import ABC, abstractmethod

class VendingMachineState(ABC):

    @abstractmethod
    def selectItem(self,name):
        pass

    @abstractmethod
    def dispense(self):
        pass

    @abstractmethod    
    def insertCoin(self,Coin):
        pass

    @abstractmethod
    def refund(self):
        pass