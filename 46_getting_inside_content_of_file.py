from tkinter import *
from tkinter.filedialog import *

a = Tk()

def mfileopen():
    file1 = askopenfile()
    label1 = Label(text=file1.name).pack()
    f = open(file1.name)
    label2 = Label(text=f.read(),bg='yellow' ,font=("roman",16,"italic")).pack()
    f.close()
    
button = Button(text="open file",width=30,command=mfileopen).pack()
a.mainloop()
