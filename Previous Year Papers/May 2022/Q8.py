# How will you add and access elements in a dictionary? WAP to concatenate the following dictionaries to create a new one.

# To add elements in a dictionary:
my_dict = {"name": "John", "age": 30}

# Accessing elements from a dictionary
for i in my_dict.values():
    print(i)

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

result_dict = {}
result_dict.update(dic1)
result_dict.update(dic2)
result_dict.update(dic3)

print(result_dict)
