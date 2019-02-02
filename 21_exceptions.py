#handling exceptions

num1 = int(input("Enter number 1:\n"))
num2 = int(input("Enter number 2:\n"))
try:            #try this thing
    num3 = num1/num2
except:         #if exception occurs    
    print("You can't divide a number by zero")
else:           #if exception doesn't occur
    print(num3)
