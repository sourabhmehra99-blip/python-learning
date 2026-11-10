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
add_button = Button(frame,text="ADD",
                    font=("Arial",15),
                    bg="#f7ffbe",
                    command=add_func)
add_button.pack()
submit_button = Button(frame,text="Submit",
                       font=("Arial",15),
                       bg="#f7ffbe",
                       command=submit_fun)
submit_button.pack()

delete_button = Button(frame,text="Delete",
                       font=("Arial",15),
                       bg="#f7ffbe",
                       command=delete_fun)
listbox.config(height=listbox.size())
delete_button.pack()

frame.pack()

listbox.config(height=listbox.size())
window.mainloop()