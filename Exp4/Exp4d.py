# Write a program that inputs a text file. The program should print the unique words in the file in alphabetical order

def unique_words(file_name):
    with open(file_name, "r") as file:
        words = file.read().split()
        unique_words = set(words)
        for word in sorted(unique_words):
            print(word)


file = input("Enter the name of the file: ")
unique_words(file)
