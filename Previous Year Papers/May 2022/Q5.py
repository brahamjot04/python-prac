# WAP to search a specific part of a string for a substring.

def search_string():
    string = input("Enter the string: ")
    sub_str = input("Enter the substring to search: ")
    if sub_str in string:
        print("Substring found")
    else:
        print("Substring not found")

search_string()