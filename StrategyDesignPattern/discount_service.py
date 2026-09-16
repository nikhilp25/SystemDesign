from discount_strategy import DiscountStrategy

class DiscountService:
    def __init__(self,strategy: DiscountStrategy):
        self.strategy = strategy

    def set_strategy(self,new_strategy: DiscountStrategy):
        self.strategy = new_strategy

    def process(self):
        self.strategy.calculate_discount()