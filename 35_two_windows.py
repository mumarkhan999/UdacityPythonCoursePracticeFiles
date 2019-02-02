#to attach button to specific window
#pass the window object also in the
#Label or Button or Entry... constructor

#if you don't pass then these buttons, labels
#will attach to the first window you will create
#e.g: in our case it is gui1

from tkinter import *
gui1 = Tk()
gui2 = Tk()
gui1.title("GUI1")
gui2.title("GUI2")
gui1.geometry("200x200+100+100")
gui2.geometry("200x200+400+100")

def display():
    gui2_label1 = Label(gui2,text=message.get(),fg='yellow',bg='black',font=10).pack()

message = StringVar()
gui1_but1 = Button(gui1,text="Enter",fg='yellow',bg='black',command=display,font=10).pack()
gui1_text1 = Entry(gui1,textvariable=message).pack()

gui1.mainloop()
gui2.mainloop()
