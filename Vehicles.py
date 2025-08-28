# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  # general method for polymorphism

# Child classes
class Car(Vehicle):
    def move(self):
        print("Car is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying ✈️")

class Bike(Vehicle):
    def move(self):
        print("Bike is pedaling 🚲")

# Testing polymorphism
vehicles = [Car(), Plane(), Bike()]
for v in vehicles:
    v.move()
