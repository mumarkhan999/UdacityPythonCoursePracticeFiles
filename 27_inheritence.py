class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return ("Name:{}\nAge:{}".format(self.name,self.age))

class teacher(person):
    def __init__(self,name,age,subj):
        person.__init__(self,name,age)
        self.subj = subj

    def __str__(self):
        return ("Name:{}\nAge:{}\nSubject:{}".format(self.name,self.age,self.subj))
