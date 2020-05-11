from tkinter import *

def changeToRed():
    labelText.set('Red')
    label.config(bg = 'red')

def changeToBlue():
    labelText.set('Blue')
    label.config(bg = 'blue')

def changeToGreen():
    labelText.set('Green')
    label.config(bg = 'green')

root = Tk()

labelText = StringVar()
labelText.set('label')

label = Label(root, textvariable = labelText)
label.pack()

Button(root, text = "Red", command = changeToRed).pack()

Button(root, text = "Green", command = changeToGreen).pack()

Button(root, text = "Blue", command = changeToBlue).pack()

root.mainloop()