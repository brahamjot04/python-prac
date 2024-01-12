import math

radius = float(input("Enter the radius of the sphere: "))

diameter = 2 * radius
circumference = round(2 * math.pi * radius, 2)
surface_area = round(4 * math.pi * radius ** 2, 2)
volume = round((4/3) * math.pi * radius ** 3, 2)

print("Diameter: ", diameter)
print("Circumference: ", circumference)
print("Surface Area: ", surface_area)
print("Volume: ", volume)
