from observer import Observer

class Mobile(Observer):
    def update(self, temp):
        print(f"Mobile shows temperature is {temp}")