from tkinter import *
root = Tk()

Frame = Frame(root)
Frame.pack()
buttonFrame = Frame
buttonFrame.pack(side=BOTTOM)
redbutton = Button(Frame, text='RED', fg='RED')
redbutton.pack(side=LEFT)
greenbutton = Button(Frame, text='Green', fg='BLUE')
greenbutton.pack(side=LEFT)
orangebutton = Button(Frame, text='Orange', fg='BROWN')
orangebutton.pack(side=RIGHT)
mainloop()
