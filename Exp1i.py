# An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any overtime pay. Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage. Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an employee’s total weekly pay.

hourly_wage = float(input("Enter hourly wage: "))
total_regular_hours = int(input("Enter total regular hours: "))
total_overtime_hours = int(input("Enter total overtime hours: "))

overtime_pay = total_overtime_hours * 1.5 * hourly_wage
weekly_pay = (hourly_wage * total_regular_hours) + overtime_pay

print("Total weekly pay: ", weekly_pay)
