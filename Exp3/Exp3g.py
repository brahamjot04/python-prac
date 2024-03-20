# Write a script named dif.py. This script should prompt the user for the names of two text files and compare the contents of the two files to see if they are the same. If they are, the script should simply output "Yes". If they are not, the script should output "No", followed by the first lines of each file that differ from each other. The input loop should read and compare lines from each file. The loop should break as soon as a pair of different lines is found.

file1 = input("Enter the name of the first text file: ")
file2 = input("Enter the name of the second text file: ")

with open(file1, 'r') as f1, open(file2, 'r') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

for line1, line2 in zip(lines1, lines2):
    if line1 != line2:
        print("No")
        print(f"First line that differs: {line1}")
        print(f"First line that differs: {line2}")
        break
else:
    print("Yes")
