from tkinter import *
from tkinter import messagebox # import messagebox module
def click():
    # messagebox.showinfo(title="this is a message box",message="you are a person")
    # messagebox.showwarning(title="Warning",message="something went wrong")
    messagebox.showerror(title="Error",message="something went wrong :(")



window = Tk()

button = Button(window,
                text="Click Me",
                command=click)
button.pack()
window.mainloop()