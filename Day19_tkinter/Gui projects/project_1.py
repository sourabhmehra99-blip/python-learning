# find problem in this code


from tkinter import *

def submit():
    username = userentry.get()
    password = passwordentry.get()
    email = email_entry.get()
    print("Username:", username)
    print("Password:", password)
    print("Email:", email)

window = Tk()
window.title("Login System")

username = Label(window,text="Username",anchor="w",font=("arial",10),padx=3,pady=3).grid(row=0,column=0)

userentry = Entry(window,width=20,font=("arial",10))
userentry.grid(row=0,column=1)

password = Label(window,text="Password",font=("arial",10),
                 padx=3,pady=3,
                 width=10,height=1).grid(row=1,column=0)

passwordentry = Entry(window,font=("arial",10),width=20)
passwordentry.grid(row=1,column=1)

email = Label(window,text="Email",font=("arial",10),width=10).grid(row=2,column=0)

email_entry = Entry(window,font=("arial",10),width=20)
email_entry.grid(row=2,column=1)

submit_button = Button(window,text="Submit",font=("arial",10),
                       width=10,command=submit,
                       ).grid(row=3,columnspan=3)

window.mainloop()