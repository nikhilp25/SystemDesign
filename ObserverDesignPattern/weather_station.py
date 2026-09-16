from observer import Observer
from typing import List

class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__observer:List[Observer] = []

    def add_observer(self,new_observer:Observer):
        self.__observer.append(new_observer)

    def remove_observer(self,observer_to_remove:Observer):
        self.__observer.remove(observer_to_remove)

    def notify_observers(self):
        for obs in self.__observer:
            obs.update(self.__temperature)

    def update_temperature(self,temp):
        self.__temperature = temp
        self.notify_observers()