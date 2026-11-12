from tkinter import *
from tkinter import filedialog

# def file():
#     filepath = filedialog.askopenfilename(title="Open file",
#                                           filetypes=(( "Text Files", "*.txt" ),( "Python Files", "*.py" )))
#     file = open(filepath,"r")
#     print(file.read())
#     file.close()
    
# window = Tk()

# button = Button(window,text="open",command=file)
# button.pack()
# window.mainloop()

# save file

window = Tk()

button = Button(window,text="save",command=lambda:filedialog.asksaveasfilename())
button.pack()
text = Text(window,font=("arial",16),fg="black")
text.pack()
window.mainloop()