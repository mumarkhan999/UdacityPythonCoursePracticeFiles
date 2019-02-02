#instead of geometry we can also use padding like padx
#anchor will make the postion stick to the specific direction
#like west in the given code
#use of padx, pady, anchor, is optional
from tkinter import *
root = Tk()
root.title("radio buttons")
r1 = Radiobutton(root, text='radio1', padx=40).pack(anchor=W)
r2 = Radiobutton(root, text='radio2', pady=40).pack(anchor=W)
r3 = Radiobutton(root, text='radio3',padx=40).pack(anchor=W)
r4 = Radiobutton(root, text='radio4',pady=40).pack(anchor=W)
root.mainloop()