# WAP that accepts a string and calculate the number of digits and letters in the string.

def count_digits_letters():
    string = input("Enter the string: ")
    digits = 0
    letters = 0
    for i in string:
        if i.isdigit():
            digits += 1
        elif i.isalpha():
            letters += 1
    print(f"Digits: {digits}\nLetters: {letters}")

count_digits_letters()