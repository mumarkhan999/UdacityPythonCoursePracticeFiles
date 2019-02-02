from tkinter import *
from tkinter.colorchooser import *

a = Tk()
def mcolor():
    color = askcolor()
    label = Label(text='your choosen color',bg=color[1]).pack()

button = Button(text="choose color",width = 30,command = mcolor).pack()
a.mainloop()
