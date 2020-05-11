from tkinter import *

def showOnLabel():
    labelText.set(entry.get())

root = Tk()

entry =Entry(root, bg = 'black', fg="yellow")
entry.pack()

Button(root, text = 'show text on label', command = showOnLabel).pack()

labelText = StringVar()
labelText.set("____________________")

label = Label(root, textvariable = labelText)
label.pack()

root.mainloop()