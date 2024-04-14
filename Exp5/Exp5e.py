# Define and test a function myRange. This function should behave like Python’s standard range function, with the required and optional arguments, but it should return a list. Do not use the range function in your implementation! (Hints: Study Python’s help on range to determine the names, positions, and what to do with your function’s parameters. Use a default value of None for the two optional parameters. If these parameters both equal None, then the function has been called with just the stop value. If just the third parameter equals None, then the function has been called with a start value as well. Thus, the first part of the function’s code establishes what the values of the parameters are or should be. The rest of the code uses those values to build a list by counting up or down.)

def myRange(start, stop=None, step=None):
    if stop is None and step is None:
        start, stop = 0, start
    elif step is None:
        start, stop, step = start, stop, 1

    result = []
    if step > 0:
        while start < stop:
            result.append(start)
            start += step
    elif step < 0:
        while start > stop:
            result.append(start)
            start += step

    return result


# Testing the myRange function
print(myRange(1, 5))  # Output: [1, 2, 3, 4]
print(myRange(1, 10, 2))  # Output: [1, 3, 5, 7, 9]
print(myRange(10, 1, -2))  # Output: [10, 8, 6, 4, 2]
