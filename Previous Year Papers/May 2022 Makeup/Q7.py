# WAP that computes and prints the average of numbers in a text file. You should make use of higher-order functions to simplify the design.

# Open the file
from functools import reduce


with open('numbers.txt', 'w') as f:
    # Write the numbers to the file
    f.write('1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n')

# Open the file
with open('numbers.txt', 'r') as f:
    numbers=f.readlines()
    # Calculate the sum of the numbers
    sum=reduce(lambda x,y: x+y, map(int, numbers))
    # Calculate the average
    average=sum/len(numbers)
    print(average)