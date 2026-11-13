from tkinter import *


def create_window():
    newwindow = Toplevel() # Toplevel() is used to create a new window it connects with older window
    newwindow.title("New Window")

    Button(newwindow,text="add name",font=("arial",20),width=10,command=lambda: print("Name added")).pack(side=TOP)


window = Tk()

window.title("New Tabs")
window.geometry("400x400")

Button(window,text="New tab",font=("arial",20),width=10,command=create_window).pack(side=TOP)

window.mainloop()