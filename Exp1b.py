# You can calculate the surface area of a cube if you know the length of an edge. Write a program that takes the length of an edge (an integer) as input and prints the cube’s surface area as output. 

edge = int(input("Enter the length of edge of cube: "))
surface_area = 6*edge**2
print("Surface area of cube is: ", surface_area)
