from tkinter import *
layout = Tk()
layout.title('Birb Generator')
layout.geometry('400x200')

label = Label(layout, text='Birb 1 >.< :', anchor='e')
label.grid(column=0, row=0)

nilai1= Entry(layout, width=10)
nilai1.grid(column=1,row=0)
label2 = Label(layout, text='Blirb :3',anchor='e')
label2.grid(column=0,row=1)
nilai2 = Entry(layout, width=10)
nilai2.grid(column=1, row=1)
label3 = Label(layout, text='birb results >:3', anchor='e')
label3.grid(column=0, row=2)

hasil = Label(layout, text='0', anchor='w', width=10)
hasil.grid(column=1, row=2)

def tambah():
    hasil.configure(text=int(nilai1.get())+int(nilai2.get()))
def kurang():
    hasil.configure(text=int(nilai1.get())-int(nilai2.get()))
def kali():
    hasil.configure(text=int(nilai1.get())*int(nilai2.get()))
btn = Button(layout, text='plus!', command=tambah)
btn.grid(column=2, row=3)

k = Button(layout, text='minus :(', command=kurang)
k.grid(column=3, row=4)
e = Button(layout, text='times', command=kali)
e.grid(column=4, row=3)

layout.mainloop()

