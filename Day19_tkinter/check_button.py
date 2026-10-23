# how to use check button


def display():
    if(x.get()=="Yes"): # don't need any compair
        print("you agree (:")
    else:
        print("you not agree :(")
from tkinter import *

window = Tk()

# x = IntVar() # use for variable makeing (1 and 0)
# x = BooleanVar() # use booleanvar (true and false)
x = StringVar() # any sting value

check = Checkbutton(window,text="I agree to you",
                    font=('Ink free',30),
                    variable=x, # using integer variable
                    onvalue="Yes", 
                    offvalue="No",
                    command=display,
                    fg="#00FF00",
                    bg="black",
                    activebackground="black",
                    activeforeground="#00FF00",
                    padx=25,
                    pady=10)
check.pack()

window.mainloop()