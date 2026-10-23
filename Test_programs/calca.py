from tkinter import *

def Ent():
    cal = display.get()
    print(cal)

def delete():
    display.delete(0,END)


window =Tk()
window.geometry("420x530")
window.title("Calculator")

display = Entry(window,font=("arial",40,'bold'))
display.config(bg="#0B140B",fg="white")
display.pack()

entry = Button(window,text="ANS",font=('arial',40),command=Ent)
entry.pack(side=RIGHT)

delete_button =Button(window,text="delete",font=('arial',40),command=delete)
delete_button.pack(side=LEFT)

window.mainloop()