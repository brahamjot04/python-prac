# Write a program that inputs a text file. The program should print the unique words in the file in alphabetical order

def unique_words(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        unique_words = set(words)
        unique_words = list(unique_words)
        unique_words.sort()
        print(unique_words)

filename = input("Enter the file name: ")
unique_words(filename)
