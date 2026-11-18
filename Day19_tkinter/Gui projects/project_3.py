# login interface 

from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Interface")
        self.geometry("320x320")
        self.frame = my_frame(self)
        self.frame.pack()
        button(self).pack()

    def submit(self):
        username = self.frame.user.get()
        password = self.frame.pas.get()
        print(f"Username: {username}, Password: {password}")

    def login(self):
        username = self.frame.user.get()
        password = self.frame.pas.get()
        print(f"Logging in with Username: {username}, Password: {password}")

class my_frame(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.label = Label(self,
                           text="Username : ",
                           font=("arial",10),
                           pady=20)
        self.label.grid(row=0,column=0)

        self.user = Entry(self,font=("arial",10))
        self.user.grid(row=0,column=1)

        self.label1 = Label(self,
                            text="password : ",
                            font=("arial",10))
        self.label1.grid(row=1,column=0)
        self.pas = Entry(self,font=("arial",10))
        self.pas.grid(row=1,column=1)

class button(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.submit = Button(self,text="sign in",
                             font=("arial",10),
                             command=parent.submit,
                             pady=2,padx=2)
        self.submit.grid(row=0,column=0,padx=10)

        self.login = Button(self,text="Login",font=("arial",10),pady=2,
                            command=parent.login)
        self.login.grid(row=0,column=1,padx=10)

    
app = App()
app.mainloop()