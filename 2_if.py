#use of simple if condition

name = input("Enter your name:\n")
age = input("Enter your age:\n")
age = int(age)
if(age <= 10):
    print(name,"is a child.")
if(age > 10 and age < 20):
    print(name,'is a young boy.')
if(age > 20 and age < 40):
    print(name,'is an adult.')
if(age > 40):
    print(name,'is an old guy.')


input("Press any key to quit...")
