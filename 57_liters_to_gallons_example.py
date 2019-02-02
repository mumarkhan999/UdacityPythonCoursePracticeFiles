from tkinter import *

def mcal():
    try:
        # to clear previous text
        e2.delete(0, END)
        var2 = var1.get()
        var3 = var2 * 3.785
    except:
        #to insert new text
        e2.insert(0, "ERROR")
    else:
        # to insert new text
        e2.insert(0, var3)

def mclear():
    e1.delete(0, END)
    e2.delete(0, END)

a = Tk()
var1 = IntVar()
n = "aerial",14,"bold"

Label(a, text="Gallons", font=(n), padx=25).grid(row=0, sticky=W)
e1 = Entry(a, width=25, textvariable=var1)
e1.grid(row=0, column=1)

Label(a, text="Litres", font=(n), padx=25).grid(row=1, sticky=W)
e2 = Entry(a, width=25)
e2.grid(row=1, column=1)

Button(text="Calculate", font=(n), width=25,command=mcal).grid(row=2, column=0)
Button(text="Clear", font=(n), width=25,command=mclear).grid(row=2, column=1)
Button(text="Quit", font=(n), width=25,command=a.destroy).grid(row=3, column=0)

a.mainloop()