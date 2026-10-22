# button from tkinter

def click():
    print('hello!!!')
from tkinter import *
window = Tk()
button =Button(window,text='Click me')
button.config(command=click)
button.config(font=('ink free',50,'bold'))
button.config(fg='red')
window.mainloop()