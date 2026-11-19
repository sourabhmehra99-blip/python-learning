# # login interface 

# from tkinter import *

# class App(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Login Interface")
#         self.geometry("320x320")
#         self.frame = my_frame(self)
#         self.frame.pack()
#         button(self).pack()

#     def submit(self):
#         username = self.frame.user.get()
#         password = self.frame.pas.get()
#         print(f"Username: {username}, Password: {password}")

#     def login(self):
#         username = self.frame.user.get()
#         password = self.frame.pas.get()
#         print(f"Logging in with Username: {username}, Password: {password}")

# class my_frame(Frame):
#     def __init__(self,parent):
#         super().__init__(parent)
#         self.label = Label(self,
#                            text="Username : ",
#                            font=("arial",10),
#                            pady=20)
#         self.label.grid(row=0,column=0)

#         self.user = Entry(self,font=("arial",10))
#         self.user.grid(row=0,column=1)

#         self.label1 = Label(self,
#                             text="password : ",
#                             font=("arial",10))
#         self.label1.grid(row=1,column=0)
#         self.pas = Entry(self,font=("arial",10))
#         self.pas.grid(row=1,column=1)

# class button(Frame):
#     def __init__(self,parent):
#         super().__init__(parent)
#         self.submit = Button(self,text="sign in",
#                              font=("arial",10),
#                              command=parent.submit,
#                              pady=2,padx=2)
#         self.submit.grid(row=0,column=0,padx=10)

#         self.login = Button(self,text="Login",font=("arial",10),pady=2,
#                             command=parent.login)
#         self.login.grid(row=0,column=1,padx=10)

    
# app = App()
# app.mainloop()

# second try of login interface ->

from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login GUI 2")
        self.geometry("320x220")

        # make a label at center in main window
        self.login_label = Label(self,text="LOGIN",font=("Segoe UI", 18, "bold"),pady=10)
        self.login_label.pack()

        # making new frame 
        new_frame = Frame(self)
        new_frame.pack()
        # Create username and password label and Entrys
        self.username = Label(new_frame,text=("Username : "),font=("arial",10),padx=10,pady=10)
        self.username.grid(row=0,column=0) 
        self.user = Entry(new_frame)
        self.user.grid(row=0,column=1)

        self.password = Label(new_frame,text=("Password : "),font=("arial",10))
        self.password.grid(row=1,column=0)
        self.pass_enter = Entry(new_frame,show="*")
        self.pass_enter.grid(row=1,column=1)
        # Create login and sign in buttons

        self.sign_in = Button(self,text="Sign In",font=("arial",10), width=15,command=self.sign_in)
        self.sign_in.pack(pady=5)

        self.login = Button(self,text="Login",font=("arial",10), width=15,command=self.login)
        self.login.pack(pady=5)
    def sign_in(self):
        username = self.user.get()
        password = self.pass_enter.get()
        print(f"{username} :{password}")
        print("succesfully Sign in")

    def login(self):
        username = self.user.get()
        password = self.pass_enter.get()
        print(f"{username} :{password}")
        print("succesfully login")



app = App()
app.mainloop()

