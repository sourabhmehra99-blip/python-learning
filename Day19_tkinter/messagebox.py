from tkinter import *
from tkinter import messagebox # import messagebox module
def click():
    # messagebox.showinfo(title="this is a message box",message="you are a person")
    # messagebox.showwarning(title="Warning",message="something went wrong")
    # messagebox.showerror(title="Error",message="something went wrong :(")

    if messagebox.askokcancel(title="askokcancel",message="do you want to continue?"):
        print("you are continuing...")
    else:
        messagebox.showwarning(title="Warning",message="you have cancelled the operation")


window = Tk()

button = Button(window,
                text="Click Me",
                command=click)
button.pack()
window.mainloop()