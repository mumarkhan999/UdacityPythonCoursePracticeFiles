from tkinter import *
my_gui = Tk()
my_gui.title("Hello")
#500x500 is the height and width
#+100+100 are the coordinates where the
#window should be loacted
#you can just give height and width like
#my_gui.geometry("500x500")
my_gui.geometry("500x500+300+100")


#the following method is to sustain the
#created window when the .exe file is run
#otherwise it will be closed simultaneously as
#it created

#this is just like we did earlier by this line
#input("Press any key to quit...")

my_gui.mainloop()
