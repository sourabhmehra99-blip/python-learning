from tkinter import *


window = Tk()
window.title("Menu Bar ")
window.geometry("400x400")

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="file",menu=filemenu)
filemenu.add_command(label="open",command=lambda:print(" file open"))
filemenu.add_command(label="New",command=lambda:print("a new file open"))
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)

Editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=Editmenu)
Editmenu.add_command(label="delete")
Editmenu.add_command(label="change")



window.mainloop()