from tkinter import *
from tkinter import messagebox

def butoonTapped():
    messagebox._show("Message", "Button Clicked")

root = Tk()

Button(root, text = "click me", command = butoonTapped).pack()

root.mainloop()