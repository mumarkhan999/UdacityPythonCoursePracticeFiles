#using different string functions
#also using : operator just like matlab


def main():
    while 1:
        my_str = input("Enter your string:")
        print("Enter 0 to display the length of a string")
        print("Enter 1 to display string from specific index to end")
        print("Enter 2 to display string from start to specific index")
        print("Enter 3 to display string from start to end with jump")
        print("Enter 4 to replace something from string")
        print("Enter 5 to convert into lower")
        print("Enter 6 to convert into upper")
        print("Enter 7 to display string for specific time")
        print("Enter 8 quit")
        choice = input("Enter your choice:")
        if(choice == "0"):
            print(len(my_str))
        elif(choice == "1"):
            start_index = int(input("Enter starting index from 0 to " + str(len(my_str)-1) + "\n"))
            print(my_str[start_index:])
        elif(choice == "2"):
            end_index = int(input("Enter ending index from 0 to " + str(len(my_str)-1) + "\n"))
            print(my_str[0:end_index])
        elif(choice == "3"):
            jump = int(input("Enter jump from 0 to " + str(len(my_str)-1) + "\n"))
            print(my_str[::jump])
        elif(choice == "4"):
            old = input("Enter old character:\n")
            new = input("Enter new character:\n")
            my_str = my_str.replace(old,new)
            print(my_str)
        elif(choice == "5"):
            my_str = my_str.lower()
            print(my_str)
        elif(choice == "6"):
            my_str = my_str.upper()
            print(my_str)
        elif(choice == "7"):
            times = int(input("Enter number of times:\n"))
            print(my_str * times)
        elif(choice == "8"):
            break
        else:
            print("Invalid choice...")
            

#calling main function
main()
