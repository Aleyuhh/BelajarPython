from tkinter import *
layout = Tk()
v = IntVar()

Radiobutton(layout, text='Guts & Blackpowder',variable = v,value=1).pack(anchor=CENTER)
Radiobutton(layout, text='Blood & Iron', variable= v, value=2).pack(anchor=CENTER)

mainloop()