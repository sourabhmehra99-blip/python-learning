# how to entry string in GUI

from tkinter import *

def submit():
    user_name = entry.get()
    print(f"hello {user_name}")

def delete():
    entry.delete(0,END)

def back():
    entry.delete(len(entry.get())-1,END)

window = Tk()
entry =Entry(window,font=('arial',40))
entry.pack(side=LEFT)

submit_button = Button(window,text='submit',command=submit)
submit_button.pack()

delete_button = Button(window,text='delete',command=delete)
delete_button.pack()

back_space = Button(window,text='backspace',command=back)
back_space.pack()
window.mainloop()