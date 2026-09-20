from cusine_factory import CuisineFactory

class RestaurantService:
    def __init__(self,factory:CuisineFactory):
        self.factory=factory
    
    def order(self):
        self.factory.create_starter().prepare()
        self.factory.create_mainCourse().prepare()
        self.factory.create_dessert().prepare()