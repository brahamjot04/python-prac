# WAP using classes and objects that simulates result preparation system for 20 students. The data available for each student include: Name, Rollno and Marks in 3 subjects. The percentage of each student is calculated and the grade is assigned based on the following criteria:
#     80 to 100: Grade A
#     60 to 80: Grade B
#     45 to 60: Grade C
#     Less than 45: Grade D

class Student:
    def __init__(self, name, rollno, marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

        self.percentage=self.calculate_percentage()
        self.grade=self.calculate_grade()

    def calculate_percentage(self):
        return sum(self.marks)/len(self.marks)
    
    def calculate_grade(self):
        percentage=self.calculate_percentage()
        if percentage>=80:
            return 'A'
        elif percentage>=60:
            return 'B'
        elif percentage>=45:
            return 'C'
        else:
            return 'D'
        
    def __str__(self):
        return f'{self.rollno} {self.name} {self.marks} {self.percentage} {self.grade}'
    

print("Rollno Name Marks Percentage Grade")

students=[]
students.append(Student('Alice', 1, [80, 90, 70]))
students.append(Student('Bob', 2, [60, 70, 80]))
students.append(Student('Charlie', 3, [45, 55, 65]))
students.append(Student('David', 4, [40, 50, 60]))
students.append(Student('Eve', 5, [80, 90, 100]))
students.append(Student('Frank', 6, [60, 70, 80]))
students.append(Student('Grace', 7, [45, 55, 65]))
students.append(Student('Harry', 8, [40, 50, 60]))
students.append(Student('Ivy', 9, [80, 90, 100]))
students.append(Student('Jack', 10, [60, 70, 80]))
students.append(Student('Katie', 11, [45, 55, 65]))
students.append(Student('Liam', 12, [40, 50, 60]))
students.append(Student('Mia', 13, [80, 90, 100]))
students.append(Student('Nathan', 14, [60, 70, 80]))
students.append(Student('Olivia', 15, [45, 55, 65]))
students.append(Student('Peter', 16, [40, 50, 60]))
students.append(Student('Quinn', 17, [80, 90, 100]))
students.append(Student('Ryan', 18, [60, 70, 80]))
students.append(Student('Sarah', 19, [45, 55, 65]))
students.append(Student('Tom', 20, [40, 50, 60]))

for student in students:
    print(student)
