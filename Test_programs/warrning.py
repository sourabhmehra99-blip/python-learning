from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Warning Message Box")

def click():
    answer =messagebox.askyesno("Warning", "do you like me?")
    if answer == True:
        messagebox.showinfo("Response", "I like you too")
    else:
        messagebox.showinfo("Response", "think again!!!")
        click()


button = Button(window,text="click me",command=click)
button.pack()
window.mainloop()