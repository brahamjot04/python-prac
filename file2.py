class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print("The vehicle is driving.")


class Bus(Vehicle):
    color = "yellow"


bus = Bus("Volvo", "red")
print("Brand: " + bus.brand)
print("Color: " + bus.color)
bus.drive()
