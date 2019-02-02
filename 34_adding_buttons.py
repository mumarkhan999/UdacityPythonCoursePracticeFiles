from tkinter import *
gui = Tk()
gui.title("GUI")
gui.geometry("500x500+200+100")
label1 = Label(text='Label 1',fg='green',bg='yellow').pack()
but1 = Button(text='Enter',fg='white',bg='black').pack()
but2 = Button(text='Enter',fg='yellow',bg='black').pack()
gui.mainloop()
