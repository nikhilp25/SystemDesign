from Starter import Starter
from main_course import MainCourse
from dessert import Dessert

class PannerTikka(Starter):
    def prepare(self):
        print("Preparing Panner Tikka")

class ButterChicken(MainCourse):
    def prepare(self):
        print("Preparing Butter Chicken")

class GulabJamun(Dessert):
    def prepare(self):
        print("Preparing Gulab Jamun")
