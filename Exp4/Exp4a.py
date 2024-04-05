# Write a program that allows the user to navigate the lines of text in a file. The program should prompt the user for a filename and input the lines of text into a list. The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. Actual line numbers range from 1 to the number of lines in the file. If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.

with open("text.txt", "r") as file:
    lines = file.readlines()
    print("The number of lines in the file is", len(lines))
    while True:
        line_number = int(input("Enter a line number (0 to quit): "))
        if line_number == 0:
            break
        elif line_number < 0 or line_number > len(lines):
            print("Invalid line number. Try again.")
        else:
            print(lines[line_number - 1].strip())
