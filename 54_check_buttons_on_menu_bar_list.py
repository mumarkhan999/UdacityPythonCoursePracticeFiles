from tkinter import *
gui1 = Tk()


def newfi():
    gui1_lab1 = Label(text='New File Entered',fg='yellow',bg='black',font=10).pack()


gui1.title("GUI1")
gui1.geometry("500x500+200+100")


gui1_menu = Menu()


#these are menu lists
list_one = Menu()
list_one.add_command(label='New File',command=newfi)
list_one.add_command(label='Open File')
#to add button use add_command
#to add check button use add_checkbutton
list_one.add_checkbutton(label='Run Mode')
list_one.add_command(label='Save')

list_two = Menu()
list_two.add_command(label='Undo')
list_two.add_command(label='Redo')

list_three = Menu()
list_three.add_command(label='Indent')
list_three.add_command(label='Dedent')

list_four = Menu()
list_four.add_command(label='Run')
list_four.add_command(label='Debug')

#adding menu option
gui1_menu.add_cascade(label="File",menu=list_one)
gui1_menu.add_cascade(label="Edit",menu=list_two)
gui1_menu.add_cascade(label="Format",menu=list_three)
gui1_menu.add_cascade(label="Run",menu=list_four)

gui1.config(menu=gui1_menu)


gui1.mainloop()
