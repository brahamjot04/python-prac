# Write a while loop that computes the factorial of a given number N

N = int(input("Enter a number: "))
fact = 1
i = 1
while i <= N:
    fact *= i
    i += 1

print(fact)
