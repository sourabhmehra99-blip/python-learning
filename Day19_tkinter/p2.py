# label = an area widget that hold the variable or an image

from tkinter import *

window = Tk()

label = Label(window,
              text="Hello World",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=10,pady=10)

# window.geometry("420x420")
# window.config(background="red")
label.pack()
# label.place(x=100,y=100)
window.mainloop()
