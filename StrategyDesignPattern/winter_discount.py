from discount_strategy import DiscountStrategy

class WinterDiscount(DiscountStrategy):
    def calculate_discount(self):
        print('Winter discount will appled')