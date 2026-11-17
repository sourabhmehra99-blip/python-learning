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

from tkinter import * # it helps to import all the classes and functions from tkinter module

class APP(Tk):              # create a class that inherits from Tk
    def __init__(self):     # initialize the class
        super().__init__()  # call the constructor of the parent class Tk
        self.title("Suprise")
        self.geometry("220x200")

        self.label = Label(self,
                           text="Suprise",
                           font=("arial",20))
        self.label.pack(pady=20)

        self.display = True     # create a boolean variable to keep track of the label's state
        self.button = Button(self,text="press",command=self.change)
        self.button.pack(pady=20)
        my_frame(self)

    def change(self):       # create a method to change the label's text when the button is pressed
        if self.display == True:
            self.label.config(text="You are the prettiest ❤️")
            self.display = False
        else:
            self.label.config(text="Surprise")
            self.display = True
            
class my_frame(Frame):      # create a class that inherits from Frame
    def __init__(self,parent):      # initialize the class, parent is the instance of the parent class APP
        super().__init__()

        self.pack(pady=20)
        self.button1 = Button(self,text="press",command=parent.change)
        self.button2 = Button(self,text="press",command=parent.change)
        self.button3 = Button(self,text="press",command=parent.change)

        self.button1.grid(row=0,column=0,padx=10)
        self.button2.grid(row=0,column=1,padx=10)
        self.button3.grid(row=0,column=2,padx=10)



app = APP()
app.mainloop()
