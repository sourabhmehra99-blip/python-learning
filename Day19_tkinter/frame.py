from tkinter import *

window = Tk()
window.title("Frame")
window.geometry("400x400")

frame = Frame(window,bg="black",relief=SUNKEN)
frame.pack()

Button(frame,text="W",font=("arial",20),width=3).pack(side=TOP)
Button(frame,text="A",font=("arial",20),width=3).pack(side=LEFT)
Button(frame,text="S",font=("arial",20),width=3).pack(side=LEFT)
Button(frame,text="D",font=("arial",20),width=3).pack(side=LEFT)
window.mainloop()