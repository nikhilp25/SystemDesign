from vending_machine_state import VendingMachineState

class IdleState(VendingMachineState):
    def __init__(self,machine):
        self.machine = machine

    def selectItem(self,name):
        print("Please wait for the current transaction to complete") 
        

    def insertCoin(self,coin):
        print("Please wait for the current transaction to complete")

    def refund(self):
        print("Please wait for the current transaction to complete")

    def dispense(self):
        print("No Item selected!")