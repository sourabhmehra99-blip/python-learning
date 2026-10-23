# making a list check button

# from tkinter import *

# skill = ['python','C++',"java"]

# window = Tk()

# x = IntVar()
# for index in range(len(skill)):
#     radio_button = Radiobutton(window,text=skill[index], # add text to radio button
#                                variable=x, # groups radio button together if they share same variable
#                                value=index, # assign each radio button a different value
#                                font=("Inpact",20),
#                                padx= 40,pady=20,
#                                indicatoron=0 ,# eleminate circle indicator
#                                #       width=222, set width
                               
#                                )
#     radio_button.pack(anchor=W)

# window.mainloop()


from tkinter import *
def choice():
    if(x.get()==0):
        print("python added in list")
    elif (x.get()==1):
        print("C++ added in list")
    elif (x.get()==2):
        print("Jave added in list")
    else:
        print("WHY!!!")
    

skill = ['python','C++',"java"]

window = Tk()

x = IntVar()
for index in range(len(skill)):
    radio_button = Radiobutton(window,text=skill[index], # add text to radio button
                               variable=x, # groups radio button together if they share same variable
                               value=index, # assign each radio button a different value
                               font=("Inpact",20),
                               padx= 40,pady=20,
                                # indicatoron=0 ,# eleminate circle indicator
                               #       width=222, set width
                               command=choice
                               )
    radio_button.pack(anchor=W)

window.mainloop()