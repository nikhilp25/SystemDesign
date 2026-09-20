from Starter import Starter
from main_course import MainCourse
from dessert import Dessert
from cusine_factory import CuisineFactory
from north_indian import PannerTikka,ButterChicken,GulabJamun

class NorthIndianCuisine(CuisineFactory):
    def create_starter(self) -> Starter:
        return PannerTikka()
    
    def create_mainCourse(self) -> MainCourse:
        return ButterChicken()
    
    def create_dessert(self) -> Dessert:
        return GulabJamun()