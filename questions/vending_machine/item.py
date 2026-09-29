class Item:
    def __init__(self, code,name,price):
        self.code = code
        self.name = name
        self.price = price

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price