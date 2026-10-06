import random
class Dice:
    def __init__(self,minValue,maxValue):
        self.minValue = minValue
        self.maxValue = maxValue

    def roll(self):
        return random.randint(self.minValue,self.maxValue)