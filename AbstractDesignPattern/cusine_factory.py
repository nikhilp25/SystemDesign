from abc import ABC, abstractmethod
from Starter import Starter
from main_course import MainCourse
from dessert import Dessert

class CuisineFactory(ABC):
    @abstractmethod
    def create_starter(self) -> Starter:
        pass

    @abstractmethod
    def create_mainCourse(self) -> MainCourse:
        pass

    @abstractmethod
    def create_dessert(self) -> Dessert:
        pass