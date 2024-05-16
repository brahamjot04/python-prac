# Write a script that should prompt user for file names of two text files and compare the contents of the two files to see if they are the same. if they are the script should print "Yes". if they are not the script should print "No", followed by the first lines of each file that differ from each other. the input loop should read and compare lines from each file. The loop should break as soon as a pair of different lines is found. 

import os

def files(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        while True:
            line1 = f1.readline()
            line2 = f2.readline()
            if line1 != line2:
                print("No")
                print(line1)
                print(line2)
                break
            if not line1:
                print("Yes")
                break

file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the second file: ")

if os.path.exists(file1) & os.path.exists(file2):
    print("Both files exist")
    files(file1, file2)

else:
    print("One or both files do not exist")



