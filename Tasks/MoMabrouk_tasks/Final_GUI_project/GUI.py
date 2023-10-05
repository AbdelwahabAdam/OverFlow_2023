from tkinter import  *
import os
from database import Database

window = Tk()
window.title("School management system")
window.geometry("450x300")
window.resizable(width="false", height="false")
# save_data = (window)
# delete_data = (window)
# update_data = (window)
selected = IntVar()
name = StringVar()
age = IntVar()
Student = ()
teacher = ()

# radio buttons
def fun():
    if selected.get() == 1:
        print ("student is selected")
    elif selected.get() == 2 : 
        print("teacher is selected")
        
student_radiobutton = Radiobutton(window, text="Student", value=1, variable= selected, command=fun)
student_radiobutton.grid(row=0, column=0)

teacher_radiobutton = Radiobutton(window, text="Teacher", value=2, variable=selected, command=fun)
teacher_radiobutton.grid(row=0, column=3)

#name and age labels and entries

name_label = Label(window, text="Name:")
name_label.grid(row=2, column=3)
name_entry = Entry(window, fg="black", textvariable= name)
name_entry.grid(row=2, column=4)

age_label = Label(window, text="Age:")
age_label.grid(row=4, column=3)
age_entry = Entry(window, fg="black", textvariable=age)
age_entry.grid(row=4, column=4)

# save button
save_button = Button(window, text="Save", command=Database.add_data)
save_button.grid(row=12, column=1)


# delete button
delete_button = Button(window, text="Delete", command=Database.delete_data)
delete_button.grid(row=12, column=3)

# Update button
delete_button = Button(window, text="Update",command=Database.update_data)
delete_button.grid(row=12, column=4)

# search label and list
search_label = Label(window, text="Search:")
search_label.grid(row=2, column=0)
search_entry = Entry(window, fg="black")
search_entry.grid(row=2, column=1)

list = Listbox(window)
list.grid(row=4, column=1)

search_entry.bind("<KeyRelease>",Database.list_data)

window.mainloop()


