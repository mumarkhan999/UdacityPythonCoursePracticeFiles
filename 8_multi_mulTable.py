#printing multiple multiplication table
num = int(input("Enter a number:\n"))
for i in range (1, (num+1)):
    print("Multiplication Table of",i)
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    
