# Write a program to count, index , reverse, sort, min and max function on list.

my_list = [5, 2, 8, 1, 9, 3, 7]

# Count the number of elements in the list
count = len(my_list)
print("Count:", count)

# Find the index of an element in the list
index = my_list.index(8)
print("Index of 8:", index)

# Reverse the list
reversed_list = my_list[::-1]
print("Reversed list:", reversed_list)

# Sort the list in ascending order
sorted_list = sorted(my_list)
print("Sorted list:", sorted_list)

# Find the minimum value in the list
minimum = min(my_list)
print("Minimum value:", minimum)

# Find the maximum value in the list
maximum = max(my_list)
print("Maximum value:", maximum)