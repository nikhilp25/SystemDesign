from order import Order 
from chef import Chef

class PizzaOrder(Order):
    def __init__(self, chef:Chef):
        self.chef = chef

    def execute(self):
        self.chef.cook_pizza()
    