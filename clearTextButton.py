from tkinter import *

def clearText():
    entry.delete(0, END)

root = Tk()

entry = Entry(root, bg = "black", fg = "yellow")
entry.pack()

Button(root, text = 'clear entry box', command = clearText).pack()

root.mainloop()