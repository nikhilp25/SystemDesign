from observer import Observer

class TV(Observer):
    def update(self, temp):
        print(f"TV shows temperature is {temp}")