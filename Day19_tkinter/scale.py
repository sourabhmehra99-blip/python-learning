from tkinter import *

window = Tk()


scale = Scale(window,from_=-100,to=100,orient=HORIZONTAL)
scale.pack()

submit = Button(window,text="Submit",command=lambda: print(f"the temprature is {scale.get()}"))
submit.pack()

window.mainloop()