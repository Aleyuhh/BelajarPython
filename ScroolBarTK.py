from tkinter import  *
layout = Tk()
scrollbar = Scrollbar(layout)
scrollbar.pack(side=RIGHT, fill=Y) #yeahhhh baby that's what we've been waiting for wooohhh
myList = Listbox(layout, yscrollcommand=scrollbar.set)
for line in range(50):
    myList.insert(END, 'niki'+str(line))
    myList.insert(END, 'blirb'+str(line))
myList.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=myList.yview())
mainloop()
