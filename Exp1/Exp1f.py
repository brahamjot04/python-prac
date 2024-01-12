# The kinetic energy of a moving object is given by the formula KE = (1 / 2)mv 2 where m is the object’s mass and v is its velocity. Modify the program you created in Project 5 so that it prints the object’s kinetic energy as well as its momentum.

mass = float(input("Enter the mass of the object (in kg): "))
velocity = float(input("Enter the velocity of the object (in m/s): "))

momentum = mass * velocity
kinetic_energy = (1/2) * mass * velocity ** 2

print("The momentum of the object is:", momentum, "kg/s")
print("The kinetic energy of the object is:", kinetic_energy, "J")
