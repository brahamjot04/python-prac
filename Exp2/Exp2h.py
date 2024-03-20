# Write a program that receives a series of numbers from the user and allows the user to press the enter key to indicate that he or she is finished providing inputs. After the user presses the enter key, the program should print the sum of the numbers and their average.


numbers = []
while True:
    user_input = input("Enter a number (or press Enter to finish): ")
    if user_input == "":
        break
    numbers.append(float(user_input))

sum_of_numbers = sum(numbers)
average = sum_of_numbers / len(numbers)

print("Sum of the numbers:", sum_of_numbers)
print("Average of the numbers:", average)
