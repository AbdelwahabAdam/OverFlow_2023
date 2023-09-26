# age calc

from tkinter import *
import tkinter as tk
import tkinter
from tkinter import *
from datetime import date


window = tkinter.Tk()


def button_submit ():

    # print("calculating")

    # ent1 = entry1.get()

    today=date.today()
    birthDate = date(int(entry1.get()), int(entry2.get()), int(entry3.get()))
    age =today.year - birthDate.year-((today.month, today.day)<(birthDate.month, birthDate.day))
    ans_label = tkinter.Label(text=f"Your age is {age}")

    ans_label.grid(row=50, column=5)





button1 = tkinter.Button(window, text= "calculate", command=button_submit)

button1.grid(row=10, column=5)

label1 = tkinter.Label(window,text= "Year: " )

label1.grid(row=0, column=0)

label1 = tkinter.Label(window,text= "Month: " )

label1.grid(row=1, column=0)

label1 = tkinter.Label(window,text= "Days: " )

label1.grid(row=2, column=0)

entry1 = tkinter.Entry(window)

entry1.grid(row=0, column=10)

entry2 = tkinter.Entry(window)

entry2.grid(row=1, column=10)

entry3 = tkinter.Entry(window)

entry3.grid(row=2, column=10)


yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

window.mainloop()