from tkinter import *
from tkinter import ttk

window = Tk()
window.title("main window")
window.geometry("400x400")

notebook = ttk.Notebook(window)
tab1= Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1,text="tab#1")
Label(tab1,text="hello,i am a coder",font=("arial",20),padx=20,pady=20).pack()

notebook.add(tab2,text="tab#2")
Label(tab2,text="hello ,this is my program",font=("arial",20),padx=20,pady=20).pack()

notebook.pack(expand=True,fill="both")


window.mainloop()