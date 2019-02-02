#self is like this pointer in C ,C# , java
#it is the object itself whose for the method is
#called


class student:
    
    #constructor
    #automatically call whenever we create an object of
    #the class
    #used to initialize the object
    #parametraised constructor
    def __init__(self,name,roll,age):
        self.name = name
        self.roll = roll
        self.age = age    
        self.attendance = 0
        self.marks = []
        
    def print_details(self):
        print("Name:{}\nRoll:{}\nAge:{}\nAttendance:{}\nMarks:{}"
              .format(self.name,self.roll,self.age,self.attendance,self.marks))

    def add_marks(self , mark):
        self.marks.append(mark)

    def add_attendance(self):
        self.attendance += 1

    def get_avg(self):
        return sum(self.marks) / len(self.marks)
    
