import tkinter
from tkinter import *
from database import Database

window = Tk()
window.geometry("700x650")

window.title("School Management System")
window.resizable(width='False',height="False")
window.geometry("400x250")


# database selecter
selected =IntVar()
def fun():
    if selected.get() == 1 :
        print("Teacher")
    elif selected.get() == 2 :
        print("student")

b1 = Radiobutton(window,text="Teacher",value=1,variable=selected , cursor="hand2",underline=True,command=fun)
b1.grid(row=0,column=1)

b2 = Radiobutton(window,text="Student",value=2,variable=selected, cursor="hand2",command=fun)
b2.grid(row=0,column=2)
selected.set(1)

# search input 
search = Label(window,text="Search :")
search.grid(row=3,column=1)

searchEnt = Entry(window)
searchEnt.grid(row=3,column=2)

db = Database(ob=Database, type='student')
db.search_data(value='45') ## any value from the object attr

#list box
items = Listbox(window,height=10)
items.grid(row= 4, column=2)
items.insert(END,"Sd1")

#data inputs

name = Label(window,text="name :")
name.grid(row=3,column=3)

nameEnt = Entry(window)
nameEnt.grid(row=3,column=4)

age = Label(window,text="age :")
age.grid(row=4,column=3)

ageEnt = Entry(window)
ageEnt.grid(row=4,column=4)

std = Database(name= "hopa", age= 45) 
db = Database(ob=std, type='student')
db.add_data()

#submit btn
def fun1 () :
    name = (nameEnt.get())
    age = int(ageEnt.get() )
    print(name , age)
    
btn1 = Button(window,text = "save",command=fun1)
btn1.grid (row=5,column=3)

db = Database(ob=Database, type='student')
db.delete_data(value='hopa', flag=1)


window.mainloop()