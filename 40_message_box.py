from tkinter import *
from tkinter import messagebox

gui1 = Tk()

def show():
    messagebox.showinfo(title='Message',message='Get lost from here')

def my_quit():
    result = messagebox.askyesno(title='quit',message='Are you sure to quit')
    if(result == 1):
        gui1.destroy()


gui1.title("GUI1")
gui1.geometry("500x500+200+100")
gui1_but1 = Button(text="Show Message",fg='yellow',bg='black',command=show,font=('times',24,'bold')).pack()
gui1_but2 = Button(text="Quit",fg='black',bg='yellow',command=my_quit,font=('times',24,'bold')).pack()
gui1.mainloop()
