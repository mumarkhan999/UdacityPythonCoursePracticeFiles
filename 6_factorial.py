#calculating factorial of a number using while loop
num = int(input("Enter any number:\n"))
if(num < 0):
    print("It's a negative number.")
else:
    fact = 1
    while(num > 0):
        fact = fact * num
        num = num - 1
    print("Answer:\t",fact)


input("Press any key to quit...")
