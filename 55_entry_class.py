from tkinter import *
a = Tk()
a.title("Hello")
Label(a, text='First Name').grid(row=0)
Label(a, text='Last Name').grid(row=1)
Label(a, text='E-mail').grid(row=2, sticky=W)
Label(a, text='Country').grid(row=3, sticky=W)
e1 = Entry(a).grid(row=0, column=1)
e2 = Entry(a).grid(row=1, column=1)
e3 = Entry(a).grid(row=2, column=1)
e4 = Entry(a).grid(row=3, column=1)



a.mainloop()