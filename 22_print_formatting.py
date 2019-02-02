#formatting with print function
#   %s for string
#   %f for float ==> to specify decimal places write %.2f  2 is for
#                       number of decimal places
#   %d for integers



name = "Haris"
age = 35
per = 65.9
#two ways to display that info
print("The age of",name,"is",age,"and his/her persentage is",per)
print("The age of %s is %s and his/her percentage is %s" %(name,age,per))
print("The age of %s is %f and his/her percentage is %f" %(name,age,per))
print("The age of %s is %.2f and his/her percentage is %.2f" %(name,age,per))
print("The age of %s is %d and his/her percentage is %d" %(name,age,per))
