from tkinter import *
from tkinter import filedialog

def file():
    filepath = filedialog.askopenfilename(title="Open file",
                                          filetypes=(( "Text Files", "*.txt" ),( "Python Files", "*.py" )))
    file = open(filepath,"r")
    print(file.read())
    file.close()
    
window = Tk()

button = Button(window,text="open",command=file)
button.pack()
window.mainloop()