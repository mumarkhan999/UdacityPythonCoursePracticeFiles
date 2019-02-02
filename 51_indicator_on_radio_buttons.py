#using indicatoron  to write text inside the radio button

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
#using list of text and value
languages = [('python',1), ('java',2), ('ruby',3), ('perl',4)]
Label(root, text='Choose any Programming \nLanguage', padx=25, justify=LEFT).pack(anchor=W)

for txt, val in languages:
    #by default indicatoron is set to 1
    #width is setted for better readablity
    Radiobutton(root, text=txt, indicatoron=0, width=25, padx=25, variable=v, command=mmm, value=val).pack(anchor=W)
root.mainloop()