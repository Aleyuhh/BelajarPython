from tkinter import *
root = Tk()
layout = Tk()
theLabel = Label(root, text='adam')
theLabel.pack()
s = Scale(layout, from_= 0, to=50)
s.pack()
s = Scale(layout, from_=0, to=2500)
s.pack()
root.mainloop()
mainloop()