#using command we are adding methods to buttons
#using Entry() to make text box

from tkinter import *
gui = Tk()

def hello():
    label2 = Label(text= message.get(),fg='green',bg='yellow',font=10).pack()



message = StringVar()
gui.title("GUI")
gui.geometry("500x500+200+100")
label1 = Label(text='Label 1',fg='green',bg='yellow',font=10).pack()
but1 = Button(text='Enter',fg='yellow',bg='black',command=hello,font=10).pack()
#can be used
#as Entry().pack
#but the following way is to get the
#text of text box
text = Entry(textvariable = message).pack()
gui.mainloop()
