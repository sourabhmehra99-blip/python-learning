from tkinter import *

window = Tk()


scale = Scale(window,from_=100,to=0,
              orient=VERTICAL, # orient gives the horizontal or vertical scale
              length=200, # it gives the length of the scale
              tickinterval = 10, # tickinterval gives the interval of the scale
              showvalue= 0, # showvalue=0 means hide the value
              resolution=5, # resolution gives the step size of the scale
              troughcolor="blue", # troughcolor gives the color of the scale
              fg="black", # fg gives the color of the text
              bg="grey"
              )
scale.set(50) # set gives the default value of the scale
scale.pack()

submit = Button(window,text="Submit",
                command=lambda: print(f"the temprature is {scale.get()}"),)
submit.pack()

window.mainloop()