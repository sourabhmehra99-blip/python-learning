# button from tkinter

# from tkinter import *

# def click():
#     print("Radha Radha")

# window = Tk()
# button =Button(window,text='Click me!!!')
# button.config(command=click)
# button.config(font=('Ink free',40,'bold'))
# button.config(bg="#FF2200")
# button.config(fg="#1ebf15")
# button.config(activebackground="#3c00ff") #it shows when the key is clicked 
# button.pack()
# window.mainloop()

# A mini program

from tkinter import *

count = 0
def click():
    global count
    count +=1
    # print(count) this will show in command panel
    label.config(text=count) # this will show on GUI on screen

window = Tk()
button = Button(window,text='click here')
button.config(command=click)
button.pack(side=BOTTOM)
label =Label(window,text=count)
label.pack()
window.mainloop()