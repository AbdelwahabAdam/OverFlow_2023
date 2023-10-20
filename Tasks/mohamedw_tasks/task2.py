from tkinter import *
import os
from database import *
from student import Student
window = Tk()


##############(Window)#######################
window.title("School Management System")
window.geometry("400x300")
window.resizable(width=FALSE,height=False)

selected =IntVar()
#############################################




##################(FUNCTIONS)#################
def add():
    x=entA.get()
    y=entN.get()
    std1= Student(name=y,age=x)
    db = Database(ob=std1, type="student")
    db.add_data()
    
def search():
    srch=ent.get()
    sname=Database(ob=srch,type="student")
    z=sname.search_data(value=srch)
    list1.insert(END,z)


def fun():
    if selected.get() == 1 :
        type1=Student(name="student: ")
        x=Database(ob=type1,type="student")
        x.add_data()

        
    elif selected.get() == 2 :
         type1=Student(name="Teacher: ")
         x=Database(ob=type1,type="teacher")
         x.add_data()
#############################################        
       
    
##############(layout)#####################
r1 = Radiobutton(window,text="student",value=1,variable=selected,command=fun)
r1.grid(row=6,column=0)

r2 = Radiobutton(window,text="teacher",value=2,variable=selected,command=fun)
r2.grid(row=6,column=2)

searchL=Label(window,text="Search: ")
searchL.grid(row=11,column=0)

nameL=Label(window,text="Name: ")
nameL.grid(row=11,column=3)
entN=Entry(window)
entN.grid(row=11,column=4)

ageL=Label(window,text="Age: ")
ageL.grid(row=15,column=3)
entA=Entry(window)
entA.grid(row=15,column=4)

ent=Entry(window)
ent.grid(row=11,column=2)

list1=Listbox(window,height=10)
list1.grid(row=15,column=2)

saveB=Button(window,text="SAVE",command=add)
saveB.grid(row=20,column=4)

serB=Button(window,text="SEARCH",command=search)
serB.grid(row=20,column=2)
################################################

window.mainloop()



