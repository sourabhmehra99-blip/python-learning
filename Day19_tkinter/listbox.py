# listbox = a listing of items that a user can select from

from tkinter import *

window = Tk()
window.title("Listbox")

listbox = Listbox(window,font=("Arial",20),bg="#f7ffbe")
listbox.pack()

listbox.insert(1,"python")
listbox.insert(2,"C++")
listbox.insert(3,"java")
listbox.insert(4,"Rust")
listbox.insert(5,"HTML")

submit_button = Button(window,text="Submit",
                       font=("Arial",20),
                       bg="#f7ffbe",
                       command=lambda: print(f"you have selected {listbox.get(listbox.curselection())}"))
submit_button.pack()

listbox.config(height=listbox.size())
window.mainloop()