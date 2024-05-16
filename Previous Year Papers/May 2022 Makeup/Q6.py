# Assume that a file contains integers separated by newlines. Write a code segment that opens the file and prints the average value of the integers. 

# Open the file
with open('numbers.txt', 'r') as f:

    numbers=f.readlines()
    sum=0
    count=0
    # Calculate the sum of the numbers  
    for number in numbers:
        sum+=int(number)
        count+=1
    
    # Calculate the average
    average=sum/count
    print(average)

