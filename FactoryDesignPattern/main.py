from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Pizza:
    def prepare(self):
        print("Preparing pizza!!!!!!!!!")

class Burger:
    def prepare(self):
        print("Preparing burger!!!!!!!!!")

class FoodFactory:
    @staticmethod
    def create_food(food_type):
        if food_type == "pizza":
            return Pizza()
        elif food_type == "burger":
            return Burger()
        else:
            raise ValueError("Invalid food type")

class ResturantService:
    def create_order(self, food_type):
        f = FoodFactory.create_food(food_type)
        f.prepare()
        return f

rs = ResturantService()
rs.create_order("pizza")
rs.create_order("burger")