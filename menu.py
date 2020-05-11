from tkinter import *

def openClicked():
    print("open was Clicked")

def quitApplication():
    quit()                      #to quit application

root = Tk()

menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu, tearoff= 0) #tearoff is used to remove - - - -line
menu.add_cascade(label = 'File', menu = subMenu)
subMenu.add_command(label = 'open', command = openClicked)
subMenu.add_separator()         # spearator is used to seprate to cascade option it add a line btw open and quit
subMenu.add_command(label = 'quit', command = quitApplication)


subMenu2 = Menu(menu, tearoff= 0)
menu.add_cascade(label = 'Edit', menu = subMenu2)
subMenu2.add_command(label = 'undo')
subMenu2.add_command(label = 'redo')

root.mainloop()