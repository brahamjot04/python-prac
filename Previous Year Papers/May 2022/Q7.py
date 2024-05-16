# Create a child class Bus which inherits all of the variables and methods from the Vehicle class.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        return f"Name: {self.name} \nMax Speed: {self.max_speed} \nMileage: {self.mileage}"
    
class Bus(Vehicle):
    pass

bus = Bus("Volvo", 180, 12)
print(bus.display())

