import tkinter as tk

counter = 0
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        #1000 ms = 1 sec
        label.after(1000,count)
    count()

root = tk.Tk()
root.title("Counter")
label = tk.Label(root , fg='dark green')
label.pack()
counter_label(label)
button = tk.Button(root,text="stop",width=40,command=root.destroy)
button.pack()
root.mainloop()




#sometimes
#lab = Label(...).pack() or
#lab = Label(...).place(...) or
#lab = Label(...).grid(...)
#does not work
#you have to separate them like this
#lab = Label(...)
#lab.pack() or lab.place(...) or lab.grid(...)

#in this code this problem occured
