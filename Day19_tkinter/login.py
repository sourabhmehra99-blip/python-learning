from tkinter import *

def password():
    pass


window = Tk()
window.title("Login GUI")
window.geometry("520x90")
window.config(bg="black")
label1 = Label(window,text='username:',font=('consolas',8))
label1.pack(side=LEFT)
username= Entry(window,font=('consolas',14),bg='white',fg="#4133BB")
username.pack()
label2 = Label(window,text='Password',font=('consolas',8))
label2.pack(side=LEFT)
password = Entry(window,font=('consolas',14),bg='white',fg="#4133BB")
password.pack()

window.mainloop()