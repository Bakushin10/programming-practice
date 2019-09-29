class PrintCreation(type):
    def __call__(self, *args, **kwargs):
        print("instance of Planet created")

class Planet(metaclass = PrintCreation):
    def __init__(self, cities):
        print(cities)
        self.cities = cities
    def sayhi(self):
        print("hi")

earth = Planet(["Paris", "Oslo"])
print(earth.sayhi())

