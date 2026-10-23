# how to use check button


def display():
    if(x.get()==1):
        print("you agree (:")
    else:
        print("you not agree :(")
from tkinter import *

window = Tk()

x = IntVar() # use for variable makeing

check = Checkbutton(window,text="I agree to you",
                    font=('Ink free',30),
                    variable=x, # using integer variable
                    onvalue=1, 
                    offvalue=0,
                    command=display,
                    fg="#00FF00",
                    bg="black",
                    activebackground="black",
                    activeforeground="#00FF00",
                    padx=25,
                    pady=10)
check.pack()

window.mainloop()