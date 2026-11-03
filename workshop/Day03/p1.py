from tkinter import *
window = Tk()
window.geometry("420x420")
window.title("MY Details")
window.configure(bg="#050B48")
window = Label(window,text="Name: Sourabh Mehra\nRoll No: 123456\nBranch: CSE\nCollege: XYZ University",
               font=("Arial",14,),
               fg="white",
               bg="#050B48",
               )
window.pack(side=LEFT,anchor="nw")
window = Label(window,text="skills: Python, C++,GIT HUB, CSS",font=("Arial",14,),fg="white",bg="#050B48")
window.pack(side=LEFT,anchor="nw")

# button = Button(window,text="Click Me")
# button.pack()

# entry = Entry(window)
# entry.pack()
window.mainloop()