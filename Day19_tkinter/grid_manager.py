from tkinter import *

window = Tk()
window.title("Info")
window.geometry("320x320")

firstname = Label(window,text="First Name",font=("arial",10)).grid(row=0,column=0)
entryname = Entry(window,width=20).grid(row=0,column=1)

phoneno = Label(window,text="Phone No",font=("arial",10)).grid(row=1,column=0)
entryphone = Entry(window,width=20).grid(row=1,column=1)

button = Button(window,text="Submit",
                font=("arial",10)).grid(row=2,column=1,columnspan=2)

window.mainloop()