# Add three methods to the Student class that compare two Student objects. One method should test for equality. A second method should test for less than. The third method should test for greater than or equal to. In each case, the method returns the result of the comparison of the two students’ names. Include a main function that tests all of the comparison operators.
# Place several Student objects into a list and shuffle it. Then run the sort method with this list and display all of the students’ information.

import random


class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name


def main():
    # Create some student objects
    student1 = Student("Alice")
    student2 = Student("Charlie")
    student3 = Student("Bob")

    # Test equality
    print(student1 == student2)  # False
    print(student1 == student1)  # True

    # Test less than
    print(student1 < student2)  # True
    print(student2 < student1)  # False

    # Test greater than or equal to
    print(student1 >= student2)  # False
    print(student2 >= student1)  # True

    # Create a list of student objects
    students = [student1, student2, student3]

    # Shuffle the list
    random.shuffle(students)

    # Sort the list
    students.sort()

    # Display all students' information
    for student in students:
        print(student.name)


if __name__ == "__main__":
    main()
