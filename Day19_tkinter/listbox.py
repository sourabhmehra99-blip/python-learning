# listbox = a listing of items that a user can select from

from tkinter import *

def add_func():
    listbox.insert(listbox.size()+1,entry.get())
    listbox.config(height=listbox.size())

def submit_fun():
    food = []
    for i in listbox.curselection():
        food.insert(i,listbox.get(i))

    print("you have selected:")
    for i in food:
        print(i)

def delete_fun():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
window = Tk()
window.title("Listbox")

listbox = Listbox(window,
                  font=("Arial",20),
                  bg="#f7ffbe",
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"python")
listbox.insert(2,"C++")
listbox.insert(3,"java")
listbox.insert(4,"Rust")
listbox.insert(5,"HTML")

entry = Entry(window,font=("Arial",20),fg="black")
entry.pack()
frame = Frame(window)
frame.pack()
add_button = Button(frame,text="ADD",height=1,width=9,
                    font=("Arial",15),
                    bg="grey",
                    command=add_func)
add_button.grid(row=0,column=0)

submit_button = Button(frame,text="Submit",height=1,width=9,
                       font=("Arial",15),
                       bg="grey",
                       command=submit_fun)
submit_button.grid(row=0,column=1)


delete_button = Button(frame,text="Delete",height=1,width=9,
                       font=("Arial",15),
                       bg="grey",
                       command=delete_fun)
listbox.config(height=listbox.size())
delete_button.grid(row=0,column=2)

backspace_button = Button(frame,text="Backspace",height=1,width=9,
                          font=("Arial",15),
                          bg="grey",
                          command=lambda: entry.delete(len(entry.get())-1,END))
backspace_button.grid(row=0,column=3)


listbox.config(height=listbox.size())
window.mainloop()