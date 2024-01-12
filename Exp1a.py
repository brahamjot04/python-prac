# The tax calculator program of the case study outputs a floating-point number that might show more than two digits of precision. Use the round function to modify the program to display at most two digits of precision in the output number.

salary = float(input("Enter the salary: "))
tax_rate = 12.5
tax = (salary*tax_rate)/100
rounded_tax = round(tax, 2)
print("Tax is: ", rounded_tax)
print("Salary after tax is: ", salary - rounded_tax)
