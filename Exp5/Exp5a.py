# A list is sorted in ascending order if it is empty or each item except the last one is less than or equal to its successor. Define a predicate isSorted that expects a list as an argument and returns True if the list is sorted, or returns False otherwise. (Hint: For a list of length 2 or greater, loop through the list and compare pairs of items, from left to right, and return False if the first item in a pair is greater.)

def isSorted(data):

    if len(data) <= 1:
        return True
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


# Test cases
print(isSorted([]))  # True
print(isSorted([1, 2, 3]))  # True
print(isSorted([2, 1]))  # False
print(isSorted([1, 3, 2]))  # False
print(isSorted(["apple", "banana", "cherry"]))  # True
print(isSorted(["cherry", "apple", "banana"]))  # False
