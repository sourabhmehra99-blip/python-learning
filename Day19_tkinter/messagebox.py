from tkinter import *
from tkinter import messagebox # import messagebox module
def click():
    messagebox.showinfo(title="this is a message box",message="you are a person") # showinfo() method is used to show information message box

    messagebox.showwarning(title="Warning",message="something went wrong") # showwarning() method is used to show warning message box

    messagebox.showerror(title="Error",message="something went wrong :(") # showerror() method is used to show error message box

    if messagebox.askokcancel(title="askokcancel",message="do you want to continue?"):# askokcancel() method is used to show ok/cancel message box
        print("you are continuing...")# it gives True or False based on the user selection
    else:
        messagebox.showwarning(title="Warning",message="you have cancelled the operation")

    answer = (messagebox.askquestion(title="ask Question",message="do you want to continue?"))# askquestion() method is used to show question message box
    if (answer =="yes"): # it gives yes or no based on the user selection
        print("you are continuing...")
    else:
        print("you have cancelled the process")
    
    answer = (messagebox.askretrycancel(title="ask Question",message="do you want to continue?"))# askretrycancel() method is used to show retry/cancel message box
    if (answer == True): # it gives True or False based on the user selection
            print("you are continuing...")
    else:
        print("you have cancelled the process")

    print(messagebox.askyesnocancel(title="ask Question",message="do you want to continue?"))# askyesnocancel() method is used to show yes/no/cancel message box ,
    # it gives three options to the user and returns True, False or None based on the user selection

window = Tk()

button = Button(window,
                text="Click Me",
                command=click)
button.pack()
window.mainloop()