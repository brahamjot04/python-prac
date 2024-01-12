mass = float(input("Enter the mass of the object (in kg): "))
velocity = float(input("Enter the velocity of the object (in m/s): "))

momentum = mass * velocity
kinetic_energy = (1/2) * mass * velocity ** 2

print("The momentum of the object is:", momentum, "kg/s")
print("The kinetic energy of the object is:", kinetic_energy, "J")
