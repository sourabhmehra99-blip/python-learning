from tkinter import *
from tkinter import filedialog

def file():
    file = filedialog.askopenfilename()
    print(file)
window = Tk()

button = Button(window,text="open",command=file)
button.pack()
window.mainloop()