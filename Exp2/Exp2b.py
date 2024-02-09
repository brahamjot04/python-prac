# WAP that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is a right triangle. Recall from the Pythagorean theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides.

side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

if (side1**2 == side2**2 == side3**2) or (side2**2 == side1**2 == side3**2) or (side3**2 == side1**2 == side2**2):
    print("This is a right angled triangle")
else:
    print("This is not a right angled triangle")
