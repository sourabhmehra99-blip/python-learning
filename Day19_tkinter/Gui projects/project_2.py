# from tkinter import *

# class App(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Object oriented programming")
#         self.geometry("400x400")
#         self.label = (Label(self,text="nice to meet you"))
#         self.label.pack()

#         self.button = Button(self,text="submit",font=("arial",10)).pack()
#         self.entry = Entry(self,font=("arial",10)).pack()
#         self.text = Text(self,font=("arial",10)).pack()
#         self.list = Listbox(self,font=("arial",10)).pack()


# app = App()
# app.mainloop()

# practice 1
from tkinter import *

class APP(Tk):
    def __init__(self):
        super().__init__()
        self.title("Suprise")
        self.geometry("220x200")

        self.label = Label(self,
                           text="Suprise",
                           font=("arial",20))
        self.label.pack(pady=20)

        self.display = True
        self.button = Button(self,text="press",command=self.change)
        self.button.pack(pady=20)

    def change(self):
        if self.display == True:
            self.label.config(text="You are the prettiest ❤️")
            self.display = False
        else:
            self.label.config(text="Surprise")
            self.display = True
            
app = APP()
app.mainloop()
