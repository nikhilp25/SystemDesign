class Inventory:
    def __init__(self):
        self.stockMap = {}
        self.itemMap = {}
    
    def addItem(self,code, item, quantity):
        self.itemMap[code] = item
        self.stockMap[code] = quantity

    def get_item(self,code):
        return self.itemMap.get(code)
    
    def is_available(self, code):
        return self.stockMap.get(code) > 0

    def reduce_stock(self, code):
        self.stockMap[code] = self.stockMap[code] - 1