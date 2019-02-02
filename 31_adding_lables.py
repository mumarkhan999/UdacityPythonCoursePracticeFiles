from tkinter import *
my_gui = Tk()
my_gui.title("My Window")
my_gui.geometry("500x500+300+100")
#.pack() is to place the label in the middle of window
label1 = Label(text='Label 1',fg='red',bg='yellow').pack()
label2 = Label(text='Label 2',fg='blue',bg='green').pack()
my_gui.mainloop()
