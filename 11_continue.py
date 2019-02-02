#using continue statement
#printing even numbers
limit = int(input("Enter limit of the series of even natural numbers:"))
limit = limit + 1
for i in range(1,limit):
    if(i%2 == 1):
        continue
    print(i)
input("Press any key to quit...")
