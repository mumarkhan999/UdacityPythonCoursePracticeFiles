from tkinter import *
root = Tk()


def mmm():
    a = v.get()
    if(a==1):
        a1 = Tk()
        a1.title("Python")
        l1 = Label(a1, text='Welcome Python', font=('aerial',20,'italic'))
        l1.pack()
    elif(a==2):
        a1 = Tk()
        a1.title("Java")
        l1 = Label(a1, text='Welcome Java', font=('aerial', 20, 'italic'))
        l1.pack()
    elif(a==3):
        a1 = Tk()
        a1.title("Ruby")
        l1 = Label(a1, text='Welcome Ruby', font=('aerial', 20, 'italic'))
        l1.pack()
    else:
        a1 = Tk()
        a1.title("Perl")
        l1 = Label(a1, text='Welcome Perl', font=('aerial', 20, 'italic'))
        l1.pack()

root.title("radio buttons actions")
v = IntVar()
v.set(1)
Label(root, text='Choose any Programming \nLanguage', padx=25, justify=LEFT).pack(anchor=W)
Radiobutton(root, text='Python', padx=25, variable=v, value=1, command=mmm).pack(anchor=W)
Radiobutton(root, text='Java', padx=25, variable=v, value=2, command=mmm).pack(anchor=W)
Radiobutton(root, text='Ruby', padx=25, variable=v, value=3, command=mmm).pack(anchor=W)
Radiobutton(root, text='Perl', padx=25, variable=v, value=4, command=mmm).pack(anchor=W)
root.mainloop()