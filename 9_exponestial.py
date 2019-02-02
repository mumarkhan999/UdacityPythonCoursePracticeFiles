#claculating power of a number
#this can be done easily by using ** operator
#for example 2 ** 3 = 8
print("Assuming that both number and power will be +ve\n")
num = int(input("Enter a number:\n"))
power = int(input("Enter power:\n"))
result = num
for i in range(1,power):
    result = result * num
print(result)
input("Press any key to quit...")
