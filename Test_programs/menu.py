# a menu Gui for a restaurant

from tkinter import *

def order_fun():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("you have ordered:")
    for order in food:
        print(order)
    print("Your order will be delivered soon.")

def add_fun():
    listbox.insert(listbox.size()+1,entry.get())
    listbox.config(height=listbox.size())

def delete_fun():
    for index in listbox.curselection():
        listbox.delete(index)

window = Tk()

listbox = Listbox(window,font=("Arial",20),
                  fg="black",
                  bg="#f7ffbe",
                  selectmode=MULTIPLE)
listbox.config(height=listbox.size())
listbox.pack()

listbox.insert(1,"Apple pie")
listbox.insert(2,"Banana shak")
listbox.insert(3,"Cake ")
listbox.insert(4,"Pasta")
listbox.insert(5,"Pizza")

entry = Entry(window,font=("arial",17),fg="black")
entry.pack()

order_button = Button(window,
                      text="Order",
                      font=("Arial",17),
                      command=order_fun)
order_button.pack()

add_button = Button(window,
                    text="Add",
                    font=("Arial",17),
                    command=add_fun)
add_button.pack()

delete_button = Button(window,text="Delete",
                       font=("Arial",17),
                       command=delete_fun)
delete_button.pack()

window.title("Menu")
window.mainloop()