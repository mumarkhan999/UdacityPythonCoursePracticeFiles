#checking age using if else 

name = input("Enter your name:\n")
age = input("Enter your age:\n")
age = int(age)
if(age < 10):
    print(name , "is a child.")
elif(age < 20):
    print(name , "is a young boy.")
elif(age < 40):
    print(name , "is an adult.")
else:
    print(name , "is an old guy.")


input("Press any key to quit...")
