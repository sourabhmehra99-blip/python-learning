from tkinter import *
# window = Tk() #instantiate an instance of a window

# window.mainloop() #place window on computer screen

# window = Tk()
# window.geometry("420x420") # geometry helps to set size of screem and dimension
# window.mainloop()

window = Tk()
window.title("MY_first_program") # title key_word help to change title in tkinter GUI
window.geometry("520x520")

"{for change icon of Tk "
"we use"
"icon =PhotoImage(file = file_name)"
"window.iconphoto(True,icon)}"
window.config(background="red") # it will help to change background colour by name and also hexadecimal value
window.mainloop()