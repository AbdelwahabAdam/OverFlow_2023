from tkinter import *


window = Tk()

fileN=""

##############(Window)#######################
window.title("School Management System")
window.geometry("400x300")
window.resizable(width=FALSE,height=False)

selected =IntVar()
##################(FUNCTIONS)#################
def search_data(self, value):
        with open(f"{self.type}.txt", 'r') as file:
            for line in file:
                if value in line:
                    print(line)
def fun():
    if selected.get() == 1 :
        fileN="std.txt"
        file1 = open("std.txt","r")
        for i in file1.readlines():
            print(i)
    elif selected.get() == 2 :
        fileN="teach.txt"
       
    
##############(Radio Button)#####################
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

saveB=Button(window,text="SAVE")
saveB.grid(row=20,column=4)


window.mainloop()



