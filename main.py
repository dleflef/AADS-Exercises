from tkinter import *


window = Tk()
window.geometry("800x526")


def bmi_calc(a,b) :

    a = float(entry_height.get())
    b = float(entry_weight.get())

    if a <= 0 or b <= 0 :
        result1 = Label(window, text=f" ", width=32, height=1, font="Verdana 24 bold", fg="blue",
                        bg="light grey")
        result1.place(x=30, y=280)
        f = Label(window, text="Wrong value, please try again!", width=25, height=1, font="Verdana 20 bold", fg="green", bg="red")
        f.place(x=140, y=380)
    else:
        a = float(entry_height.get())
        b = float(entry_weight.get())

    bmi = (b / (a * a))

    if a > 0 and b > 0:
        result1 = Label(window, text = f"Your BMI is, {str(bmi)}", width=32 , height=1, font="Verdana 24 bold",fg="blue",bg="light grey")
        result1.place(x=30, y=280)


    if a > 0 and b > 0:
        if 25 > float(bmi) >= 18.5 :
            n = Label(window, text="Your BMI is normal", width=25, height=1, font="Verdana 20 bold",fg="green",bg="light grey")
            n.place(x=140, y=380)

        elif 30 > float(bmi) >= 25 :
            o = Label(window, text="You are overweighted", width=25, height=1, font="Verdana 20 bold",fg="red",bg="light grey")
            o.place(x=140, y=380)
        elif 0 < float(bmi) < 18.5 :
            u = Label(window, text="You are underweighted", width=25, height=1, font="Verdana 20 bold",fg="red",bg="light grey")
            u.place(x=140, y=380)
        elif float(bmi) >= 30 :
            u = Label(window, text="You might be obese", width=25, height=1, font="Verdana 20 bold", fg="red",bg="light grey")
            u.place(x=140, y=380)







title = Label(window, text = "WELCOME TO THE BMI CALCULATOR !", width=33 , height=1, font="Helvetica 18 bold",bg="light grey")
title.place(x=130, y=20)

height = Label(window, text = "Please enter your height: ",  font="Verdana 10", fg = "black", bg="orange")
height.place(x=150, y=95)
a=DoubleVar()
entry_height = Entry(window, textvariable=a, width=4, bg="light blue")
entry_height.place(x=336, y=97)


weight = Label(window, text = "Please enter your weight: ",  font="Verdana 10", fg = "black", bg="yellow")
weight.place(x=150, y=150)
b=DoubleVar()
entry_weight = Entry(window, textvariable=b,  width=4, bg="light blue")
entry_weight.place(x=336, y=152)


work = Button(window, text="Calculate Your\n BMI", font="Verdana 16 bold", bg="light green", command = lambda: bmi_calc(entry_height, entry_weight))
work.place(x=510, y=100)



t1 = Label(window, text = "(meters)", width=7 , height=1, font="Verdana 8 ",bg="light grey")
t1.place(x=370, y=97)
t2 = Label(window, text = "(kg)", width=3 , height=1, font="Verdana 8 ",bg="light grey")
t2.place(x=370, y=150)



window.mainloop()

