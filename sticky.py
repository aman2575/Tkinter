from tkinter import *
from tkinter import ttk

root = Tk()

label1= Label(root, text = 'Label1', bg = 'red')        #ipad is used for inner padding
label1.grid(row = 0, column = 0, ipadx =50, ipady = 50) #padx provide padding for x-axis
                                                        #pady provide padding for y-axis
label2= Label(root, text = 'Label2', bg = 'blue')       # using N S W E (north,south,east,west) diresction
                                                        
label2.grid(row = 0, column = 1, sticky= E + W)

label3= Label(root, text = 'Label3', bg = 'green')
label3.grid(row = 1, column = 0, sticky= S)

label4= Label(root, text = 'Label4', bg = 'yellow')
label4.grid(row = 1, column = 1, ipadx =50, ipady = 50)


root.mainloop()