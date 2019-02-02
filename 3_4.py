#checking greater number among 3 numbers using if else

n1 = int(input ("Enter first number:\n"))
n2 = int(input ("Enter second number:\n"))
n3 = int(input ("Enter third number:\n"))

if((n1>n2) & (n1>n3)):
    print(n1,"is greater.")
elif((n2>n1) & (n2>n3)):
    print(n2,"is greater.")
elif((n3>n1) & (n3>n2)):
    print(n3,"is greater.")
else:
    print("nobody is greater.")

input("Press any key to quit...")
