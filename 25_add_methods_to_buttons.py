#using command we are adding methods to buttons

from tkinter import *
gui = Tk()

def hello():
    label3 = Label(text='Entered',fg='green',bg='yellow',font=10).pack()
def dele():
    label4 = Label(text='deleted',fg='green',bg='yellow',font=10).pack()
    

gui.title("GUI")
gui.geometry("500x500+200+100")
label1 = Label(text='Label 1',fg='green',bg='yellow',font=10).pack()
but1 = Button(text='Enter',fg='white',bg='black',command=hello,font=10).pack()
but2 = Button(text='Delete',fg='yellow',bg='black',command=dele,font=10).pack()
gui.mainloop()
