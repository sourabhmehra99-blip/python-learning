from tkinter import *
from tkinter import messagebox # import messagebox module
def click():
    # messagebox.showinfo(title="this is a message box",message="you are a person")
    # messagebox.showwarning(title="Warning",message="something went wrong")
    # messagebox.showerror(title="Error",message="something went wrong :(")

    # if messagebox.askokcancel(title="askokcancel",message="do you want to continue?"):
    #     print("you are continuing...")
    # else:
        # messagebox.showwarning(title="Warning",message="you have cancelled the operation")
    answer = (messagebox.askquestion(title="ask Question",message="do you want to continue?"))
    if (answer =="yes"):
        print("you are continuing...")
    else:
        print("you have cancelled the process")
    
    answer = (messagebox.askretrycancel(title="ask Question",message="do you want to continue?"))
    if (answer == True):
            print("you are continuing...")
    else:
        print("you have cancelled the process")

    print(messagebox.askyesnocancel(title="ask Question",message="do you want to continue?"))
    



window = Tk()

button = Button(window,
                text="Click Me",
                command=click)
button.pack()
window.mainloop()