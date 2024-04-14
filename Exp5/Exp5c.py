# Write a recursive function that expects a pathname as an argument. The pathname can be either the name of a file or the name of a directory. If the pathname refers to a file, its name is displayed, followed by its contents. Otherwise, if the pathname refers to a directory, the function is applied to each name in the directory. Test this function in a new program.

import os


def display_file_contents(path):
    if os.path.isfile(path):
        print("File:", path)
        with open(path, 'r') as file:
            contents = file.read()
            print(contents)
    elif os.path.isdir(path):
        print("Directory:", path)
        for name in os.listdir(path):
            display_file_contents(os.path.join(path, name))


# Test the function
pathname = input("Enter the pathname: ")
display_file_contents(pathname)
