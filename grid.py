from tkinter import *
from tkinter import ttk

root = Tk()

label1= Label(root, text = 'Label1', bg = 'red')
label1.grid(row = 0, column = 0)

label2= Label(root, text = 'Label2', bg = 'blue')
label2.grid(row = 0, column = 1)

label3= Label(root, text = 'Label3', bg = 'green')
label3.grid(row = 1, column = 0)

label4= Label(root, text = 'Label4', bg = 'yellow')
label4.grid(row = 1, column = 1)

root.mainloop()