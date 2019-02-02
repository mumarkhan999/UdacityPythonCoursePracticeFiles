from tkinter import *
gui1 = Tk()
gui1.title("GUI1")
gui1.geometry("500x500+200+100")


gui1_menu = Menu()

gui1_menu.add_cascade(label="File")
gui1_menu.add_cascade(label="Edit")
gui1_menu.add_cascade(label="Format")
gui1_menu.add_cascade(label="Run")

gui1.config(menu=gui1_menu)



gui1.mainloop()
