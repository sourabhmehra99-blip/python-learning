from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Object oriented programming")
        self.geometry("400x400")
        self.label = (Label(self,text="nice to meet you"))
        self.label.pack()

        self.button = Button(self,text="submit",font=("arial",10)).pack()
        self.entry = Entry(self,font=("arial",10)).pack()
        self.text = Text(self,font=("arial",10)).pack()
        self.list = Listbox(self,font=("arial",10)).pack()


app = App()
app.mainloop()