from tkinter import *
master = Tk()
var1 = IntVar()
var2 = IntVar()
leol = Tk()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
Checkbutton(master, text='female', variable=var1).grid(row=1, sticky=W)
mainloop()