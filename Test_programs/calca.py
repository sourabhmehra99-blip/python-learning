# from tkinter import *

# def Ent():
#     cal = display.get()
#     print(cal)

# def delete():
#     display.delete(0,END)

# def back():
#     display.delete(len(display.get())-1,END)


# window =Tk()
# window.geometry("420x530")
# window.title("Calculator")

# display = Entry(window,font=("arial",40,'bold'))
# display.config(bg="#0B140B",fg="white")
# display.pack()

# entry = Button(window,text="ANS",font=('arial',40),command=Ent)
# entry.pack(side=RIGHT)

# back_button =Button(window,text="backspace",font=("Arial",40),command=back)
# back_button.pack()

# delete_button =Button(window,text="delete",font=('arial',40),command=delete)
# delete_button.pack(side=LEFT)

# window.mainloop()

from tkinter import *

def button_press(num):
    global expression_text

    expression_text = expression_text + str(num)

    expression_label.set(expression_text)

def equal():
    global expression_text
    try:
        total = str(eval(expression_text))
        expression_label.set(total)
        expression_text = total
    except SyntaxError:
        expression_label.set("syntax error")
        expression_text =''
    except ZeroDivisionError:
        expression_label.set("arthmetic error")
        expression_text = ''

def clear():
    global expression_text

    expression_label.set('')
    expression_text = ''

window = Tk()
window.title("simple calculator")
window.geometry("600x600")

expression_text = ""
expression_label= StringVar()

label = Label(window,textvariable=expression_label,
              font=('consolas',20),
              bg='white',
              background="gray",
              width=31,height=3)
label.pack()

# entry = Entry(window,font=("consolas",20))
# entry.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,text=1,height=4,width=9,font=35,
                 command=lambda: button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame,text=2,height=4,width=9,font=35,
                 command=lambda: button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame,text=3,height=4,width=9,font=35,
                 command=lambda: button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text=4,height=4,width=9,font=35,
                 command=lambda: button_press(4))
button4.grid(row=1,column=0)

button5= Button(frame,text=5,height=4,width=9,font=35,
                 command=lambda: button_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame,text=6,height=4,width=9,font=35,
                 command=lambda: button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame,text=7,height=4,width=9,font=35,
                 command=lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame,text=8,height=4,width=9,font=35,
                 command=lambda: button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame,text=9,height=4,width=9,font=35,
                 command=lambda: button_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame,text=0,height=4,width=9,font=35,
                 command=lambda: button_press(0))
button0.grid(row=3,column=0)

plus = Button(frame,text='+',height=4,width=9,font=35,
              command=lambda: button_press('+'))
plus.grid(row=0,column=3)

subtract = Button(frame,text='-',height=4,width=9,font=35,
              command=lambda: button_press('-'))
subtract.grid(row=1,column=3)

multiply = Button(frame,text='x',height=4,width=9,font=35,
              command=lambda: button_press('*'))
multiply.grid(row=2,column=3)

divide = Button(frame,text='/',height=4,width=9,font=35,
              command=lambda: button_press('/'))
divide.grid(row=3,column=3)

equal = Button(frame,text="=",height=4,width=9,font=30,
               command=equal)
equal.grid(row=3,column=2)

decimal = Button(frame,text=".",height=4,width=9,font=30,
               command=lambda: button_press('.'))
decimal.grid(row=3,column=1)

clear = Button(window,text='clear',height=9,width=11,font=30,
               command=clear)
clear.pack()




window.mainloop()