from tkinter import *
my_gui = Tk()
my_gui.title("My Window")
my_gui.geometry("500x500+200+100")
#as label2 's width is greater so column size
#will be according to label2
#and label1 will be in the middle of row 0 column 0
#sticky is to place label 1 to west side instead of middle

#you may check this line with out using sticky
#to check the above mentioned issue
#label1 = Label(text='Name',fg='red',bg='yellow').grid(row=0,column=0)
label1 = Label(text='Name',fg='red',bg='yellow').grid(row=0,column=0,sticky='w')
label2 = Label(text='Nationality',fg='blue',bg='green').grid(row=1,column=0)
my_gui.mainloop()



#sometimes
#lab = Label(...).pack() or
#lab = Label(...).place(...) or
#lab = Label(...).grid(...)
#does not work
#you have to separate them like this
#lab = Label(...)
#lab.pack() or lab.place(...) or lab.grid(...)
