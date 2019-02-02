#all magic (special) function names
#starts and ends with __  double underscore
#e.g.  __init__()  constructor

class person:

    #constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Welcome {}".format(name))

    #overrriding toString(like java) function
    def __str__(self):
         return ("Name:{}\nAge:{}".format(self.name,self.age))
    
    #de allocater like distructor
    def __del__(self):
        print("{} is deleted".format(self.name))



p1 = person("Ali",23)
p2 = person("Asif",24)
print(p1)
print(p2)
del(p1)
del(p2)
