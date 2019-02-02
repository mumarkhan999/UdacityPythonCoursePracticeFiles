#if you want to use other methods of
#Entry, Label, Button e.tc
#then declare themin this way
'''

e1 = Entry(...)
e1.grid(...)
e1.insert(...)


not like this

e1 = Entry(...).grid(...)
e1.insert(...)

otherwise error will occur


'''

from tkinter import *

def clear():
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


a = Tk()
a.title("Hello")
Label(a, text='First Name').grid(row=0)
Label(a, text='Last Name').grid(row=1)
Label(a, text='E-mail').grid(row=2, sticky=W)
Label(a, text='Country').grid(row=3, sticky=W)
e1 = Entry(a)
e1.grid(row=0, column=1)
e1.insert(0,"peter")
e2 = Entry(a)
e2.grid(row=1, column=1)
e2.insert(0,"john")
e3 = Entry(a)
e3.grid(row=2, column=1)
#we can also use variables
email = "joahn@gmail.com"
e3.insert(0,email)
e4 = Entry(a)
e4.grid(row=3, column=1)
e4.insert(0,"America")
Button(a, text="clear all", command=clear).grid(row=4, column=1, sticky=E)


a.mainloop()