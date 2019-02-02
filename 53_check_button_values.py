#at first values of var1, var2, var3, var4 will be zero
#when you will check the boxes it will cahnge into 1
from tkinter import *
def mget():
    print(var1.get(),var2.get(),var3.get(),var4.get())

a =Tk()
var1 = IntVar()
Checkbutton(a, text='But 1', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(a, text='But 2', variable=var2).grid(row=1, sticky=W)
var3 = IntVar()
Checkbutton(a, text='But 3', variable=var3).grid(row=2, sticky=W)
var4 = IntVar()
Checkbutton(a, text='But 4', variable=var4).grid(row=3, sticky=W)
Button(a, text="Get Values of Check Boxes", command=mget, width=25).grid(row=4, sticky=W)
#quit is to finish the program
#destroy is to close the window
Button(a, text="quit", command=a.quit, width=25).grid(row=5, sticky=W)
a.mainloop()