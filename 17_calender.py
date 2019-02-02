import calendar

print("Enter 1 to check that year is leap or not")
print("Enter 2 display month of specific year")
print("Enter 3 to display calaendar of specific year")
choice = input("Enter choice...")
if(choice == "1"):
    year = int(input("Enter year:\n"))
    print(calendar.isleap(year))
elif(choice == "2"):
    month= int(input("Enter month:\n"))
    year = int(input("Enter year:\n"))
    print(calendar.month(year,month))
elif(choice == "3"):
    year = int(input("Enter year:\n"))
    #calendar.calendar(year,max width b/w each charcter,lines per week,spaces b/w months)
    print(calendar.calendar(year,2,1,10))
else:
    print("nothing")
