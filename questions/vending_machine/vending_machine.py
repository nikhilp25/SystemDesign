from item import Item
from idle_state import IdleState
from inventory import Inventory
import inventory
class VendingMachine:
    _instance = None
    
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super(VendingMachine, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not hasattr(self,"_initialized") or not self._initialized:
            self.inventory = Inventory()
            self.state = IdleState(self)
            self.balance = 0
            self.selectedItemCode = None
            self.initialized = True

    @classmethod
    def get_instance(cls):
        return cls()
    
    def insert_coin(self,coin):
        self.state.insertCoin(coin)

    def select_item(self,code):
        self.state.selectItem(code)
    
    def add_item(self,code, name,price, quantity):
        item = Item(code, name,price)
        self.inventory.addItem(code, item, quantity)
        return item
    def dispense(self):
        self.state.dispense()
    
    # def dispense_item(self):
    def refund_balance(self):
        print(f"Refunding: {self.balance}")
        self.balance = 0
    
    def add_balance(self, value):
        self.balance += value
    
    def set_seleced_item_code(self,code):
        self.selectedItemCode = code

    def get_balance(self):
        return self.balance
    
    def get_inventory(self):
        return self.inventory
    
    def set_state(self,state):
        self.state = state
    
    def get_state(self):
        return self.state

    def get_selected_item_code(self):
        return self.selectedItemCode
    
    def is_valid_item(self,code):
        return self.inventory.is_available(code)
    
    def get_item_price(self,code):
        return self.inventory.get_item(code).get_price()