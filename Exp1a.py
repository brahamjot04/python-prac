salary = float(input("Enter the salary: "))
tax_rate = 12.5
tax = (salary*tax_rate)/100
rounded_tax = round(tax, 2)
print("Tax is: ", rounded_tax)
print("Salary after tax is: ", salary - rounded_tax)
