#using place method

from tkinter import *
my_gui = Tk()
my_gui.title("My Window")
my_gui.geometry("500x500+300+100")
#.place() is to place the label at specific coordinates
label1 = Label(text='Label 1',fg='red',bg='yellow').place(x=100,y=100)
label2 = Label(text='Label 2',fg='blue',bg='green').place(x=200,y=100)
my_gui.mainloop()
