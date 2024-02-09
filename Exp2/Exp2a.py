# WAP that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is an equilateral triangle.

side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

if (side1 == side2 == side3):
    print("This is an equilateral traingle")
else:
    print("This is not an equilateral triangle")
