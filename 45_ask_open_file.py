from tkinter import *
from tkinter.filedialog import *

a = Tk()

def mfileopen():
    file1 = askopenfile()
    label = Label(text=file1.name).pack()

button = Button(text="open file",width=30,command=mfileopen).pack()
a.mainloop()
