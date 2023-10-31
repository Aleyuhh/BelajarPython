from tkinter import *

master = Tk()
w = canvas(master, witdh =1370, height =768)
w.pack()
canvas_height = 40
canvas_width = 200
y = int(canvas_height/2)
w.create_line(0,y,canvas_width,y)
mainloop()
