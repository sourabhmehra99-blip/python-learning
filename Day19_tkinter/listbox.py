# listbox = a listing of items that a user can select from

from tkinter import *

window = Tk()
window.title("Listbox")

listbox = Listbox(window,font=("consolas",30),
                  bg="#f7ffde")
listbox.pack()

listbox.insert(1,"OPPM book")
listbox.insert(2,"Maths book")
listbox.insert(3,"Evs book")
listbox.insert(4,"SSC book")
listbox.insert(5,"IT book")

submit = Button(window,text="submit", # listbox.get(listbox.curselection()) <-- this will give the selected item from the listbox
                command=lambda: print(f"you have selected {listbox.get(listbox.curselection())}"))
submit.pack()

listbox.config(height=listbox.size()) # height gives the number of items to be displayed in the listbox
window.mainloop()