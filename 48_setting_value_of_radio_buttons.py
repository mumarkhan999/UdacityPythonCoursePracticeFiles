#settting default value of radio buttons
from tkinter import *
root = Tk()
root.title("radio buttons")
v = IntVar()
#setting value of radio button by its value
v.set(3)
Label(root, text='Choose a Programming \nLanguage', padx=25, justify=LEFT).pack(anchor=W)
Radiobutton(root, text='Python', padx=25, variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Perl', padx=25, variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='C Language', padx=25, variable=v, value=3).pack(anchor=W)
Radiobutton(root, text='Ruby', padx=25, variable=v, value=4).pack(anchor=W)
root.mainloop()
