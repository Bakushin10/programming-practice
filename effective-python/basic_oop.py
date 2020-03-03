class Vehicle:

  def __init__(self, num_wheels):
    self.num_wheels = num_wheels

  def slowDown(self):
    # This will be implemented in each derived class
    # since each type of vehicle stops differently
    # This is polymorphism in action!
    raise NotImplementedError



class Car(Vehicle):
  def __init__(self):
    # Here we call the parent's constructor
    super().__init__(4)

  def slowDown(self):
    # We apply encapsulation since as a car User
    # we only need to worry about using the brakes,
    # and not how they work
    self.__applyBrakes()

  def __applyBrakes(self):
    print("applying car brakes")



class Motorbike(Vehicle):
  def __init__(self):
    # Here we call the parent's constructor
    super().__init__(2)
    
  def slowDown(self):
    self.__applyFrontBrakes()
    self.__applyRearBrakes()

  def __applyFrontBrakes(self):
    print("applying front brakes")

  def __applyRearBrakes(self):
    print("applying rear brakes")


car = Car()
bike = Motorbike()

car.slowDown()
bike.slowDown()

print(isinstance(car, Car))
print(isinstance(car, Vehicle))
print(isinstance(car, object))
print(isinstance(car, Motorbike))