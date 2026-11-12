from tkinter import *

window = Tk()

text = Text(window,font=("arial",16),
            height=8,width=20,
            bg="light yellow",fg="black",
            padx=10,pady=10,)
text.pack()
frame = Frame(window)
button = Button(frame,text="submit",font=("arial",16),command=lambda:print(text.get("1.0",END)))

button.grid(row=0,column=0)
delete_button = Button(frame,text="Delete",font=("arial",16),command= lambda:text.delete("1.0",END))
delete_button.grid(row=0,column=1)
back_space = Button(frame,text="Backspace",font=("arial",16),command= lambda:text.delete("end-2c",END))
back_space.grid(row=0,column=2)

frame.pack()

window.mainloop()