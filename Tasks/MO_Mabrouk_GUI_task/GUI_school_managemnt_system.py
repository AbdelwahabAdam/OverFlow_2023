import tkinter as tk
import os

class SaveData():
    def __init__(self, window):
        self.window = window
        self.selected = tk.IntVar()
        self.name = tk.StringVar()
        self.age = tk.IntVar()

        # search label and list
        self.search_label = tk.Label(self.window, text="Search:")
        self.search_label.grid(row=2, column=0)
        self.search_entry = tk.Entry(self.window, fg="black")
        self.search_entry.grid(row=2, column=1)

        self.list = tk.Listbox(self.window)
        self.list.grid(row=4, column=1)

        self.search_entry.bind("<KeyRelease>", self.update_list)

        #name and age labels and entries
        self.name_label = tk.Label(self.window, text="Name:")
        self.name_label.grid(row=2, column=3)
        self.name_entry = tk.Entry(self.window, fg="black", textvariable=self.name)
        self.name_entry.grid(row=2, column=4)

        self.age_label = tk.Label(self.window, text="Age:")
        self.age_label.grid(row=4, column=3)
        self.age_entry = tk.Entry(self.window, fg="black", textvariable=self.age)
        self.age_entry.grid(row=4, column=4)

        # save button
        self.save_button = tk.Button(self.window, text="Save", command=self.save_data)
        self.save_button.grid(row=12, column=3)

        # radio buttons
        self.student_radiobutton = tk.Radiobutton(self.window, text="Student", value=1, variable=self.selected, command=self.fun)
        self.student_radiobutton.grid(row=0, column=0)

        self.teacher_radiobutton = tk.Radiobutton(self.window, text="Teacher", value=2, variable=self.selected, command=self.fun)
        self.teacher_radiobutton.grid(row=0, column=3)

    def fun(self):
        pass

    def save_data(self):
        if self.selected.get() == 1:
            with open("Student_data.txt", "a") as f:
                f.write(f"{self.name.get()},{self.age.get()}\n")
        elif self.selected.get() == 2:
            with open("Teacher_data.txt","a") as f:
                f.write(f"{self.name.get()},{self.age.get()}\n")

    def update_list(self, event):
        search_term = self.search_entry.get()
        self.list.delete(0, tk.END)

        if self.selected.get() == 1:
            filename = "Student_data.txt"
        else:
            filename = "Teacher_data.txt"

        with open(filename, "r") as f:
            for line in f:
                name, age = line.strip().split(",")
                if search_term in name:
                    self.list.insert(tk.END, f"{name} ({age})")

if __name__ == "__main__":
    window = tk.Tk()
    window.title("School management system")
    window.geometry("450x300")

    save_data = SaveData(window)

    window.mainloop()