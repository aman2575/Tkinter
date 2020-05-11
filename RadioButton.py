from tkinter import *

def showValue():
    print(radioButtonValue.get())

root = Tk()

radioButtonValue = StringVar()

Label(root, text = "What is the favourite weather?").pack()
Radiobutton(root, text = 'sunny', value ='sunny', variable = radioButtonValue).pack()
Radiobutton(root, text = 'rainy', value ='rainy', variable = radioButtonValue).pack()
Radiobutton(root, text = 'wet', value ='wet', variable = radioButtonValue).pack()
Radiobutton(root, text = 'dry', value ='dry', variable = radioButtonValue).pack()
Radiobutton(root, text = 'cloudy', value ='cloudy', variable = radioButtonValue).pack()

Button(root, text = "show radio button value", command = showValue).pack()

root.mainloop()