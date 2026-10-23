# making a list check button

from tkinter import *

skill = ['python','C++',"java"]

window = Tk()

x = IntVar()
for index in range(len(skill)):
    radio_button = Radiobutton(window,text=skill[index], # add text to radio button
                               variable=x, # groups radio button together if they share same variable
                               value=index, # assign each radio button a different value
                               font=("Inpact",20),
                               padx= 40,pady=20,
                               )
    radio_button.pack(anchor=W)

window.mainloop()