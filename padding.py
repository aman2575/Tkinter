from tkinter import *
from tkinter import ttk

root = Tk()

label1= Label(root, text = 'Label1', bg = 'red')  
label1.grid(row = 0, column = 0, padx=20, pady=20) 

label2= Label(root, text = 'Label2', bg = 'blue')
label2.grid(row = 0, column = 1, ipadx=20, ipady=20)

label3= Label(root, text = 'Label3', bg = 'green')
label3.grid(row = 1, column = 0, ipadx=40, ipady=40)

label4= Label(root, text = 'Label4', bg = 'yellow')
label4.grid(row = 1, column = 1, ipadx=30, ipady=30)

root.mainloop()