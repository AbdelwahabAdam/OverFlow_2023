from tkinter import *
import uuid
import os

class SMA:
    def __init__(self, window):
        self.window = window
        self.window.title("SMA")

        bg_color = "#EBE4D1"
        frame_color = "#B4B4B3"
        label_color = "#26577C"
        button_color = "#E55604"
        text_color = "#26577C"

        self.window.configure(bg=bg_color)

        top_frame = Frame(self.window, bg=bg_color)
        top_frame.pack(side=TOP, fill=X, padx=20, pady=10)

        left_frame = Frame(self.window, bg=bg_color)
        left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=10)

        right_frame = Frame(self.window, bg=bg_color)
        right_frame.pack(side=RIGHT, padx=20, pady=10)

        self.selected = IntVar()
        self.uuid = None 
        self.name = StringVar()
        self.age = IntVar()

        student_button = Radiobutton(top_frame, text="Student", value=1, variable=self.selected, command=self.update_Listbox, bg=bg_color, fg=text_color, selectcolor=bg_color)
        student_button.pack(side=LEFT, padx=10)
        teacher_button = Radiobutton(top_frame, text="Teacher", value=2, variable=self.selected, command=self.update_Listbox, bg=bg_color, fg=text_color, selectcolor=bg_color)
        teacher_button.pack(side=LEFT, padx=10)

        name_label = Label(right_frame, text="Name:", bg=bg_color, fg=label_color)
        name_label.pack()
        name_entry = Entry(right_frame, textvariable=self.name, bg=frame_color, fg=text_color)
        name_entry.pack()
        age_label = Label(right_frame, text="Age:", bg=bg_color, fg=label_color)
        age_label.pack()
        age_entry = Entry(right_frame, textvariable=self.age, bg=frame_color, fg=text_color)
        age_entry.pack()

        save_button = Button(right_frame, text="Save", command=self.save_data, bg=button_color)
        save_button.pack()
        self.delete_button = Button(right_frame, text="Delete", command=self.delete_data, bg=button_color)
        self.delete_button.pack()
        self.delete_button.config(state=DISABLED)



        self.list = Listbox(left_frame, bg=frame_color, fg=text_color)
        self.list.pack(fill=BOTH, expand=True)
        self.list.bind("<Double-Button-1>", self.load_selected_data)  

        search_label = Label(left_frame, text="Search:", bg=bg_color, fg=label_color)
        search_label.pack()
        self.search_entry = Entry(left_frame, fg=text_color,bg=frame_color)
        self.search_entry.pack(pady=5)
        self.search_entry.bind("<KeyRelease>", self.update_Listbox)

    def save_data(self):
        print("save_data")
        if self.selected.get() == 1:
            filename = "students.txt"
        elif self.selected.get() == 2:
            filename = "teachers.txt"
        else:
            return

        LB_list = []

        try:
            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:  
                        _uuid, name, age = parts
                        if _uuid == self.uuid:
                            name = self.name.get()
                            age = self.age.get()
                        LB_list.append((_uuid, name, age))

            with open(filename, "w") as f:
                for _uuid, name, age in LB_list:
                    f.write(f"{_uuid},{name},{age}\n")

            
            if self.uuid is None:
                self.uuid = str(uuid.uuid4())
                name = self.name.get()
                age = self.age.get()
                with open(filename, "a") as f:
                    f.write(f"{self.uuid},{name},{age}\n")

            self.clear_input_fields()
            
            self.update_Listbox()

        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            
    def update_Listbox(self, event=None):
        print("update_lb")
        search_term = self.search_entry.get()
        self.list.delete(0, END)

        if self.selected.get() == 1:
            filename = "students.txt"
        elif self.selected.get() == 2:
            filename = "teachers.txt"
        else:
            return

        try:
            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3: 
                        _uuid, name, age = parts
                        if search_term in name:
                            self.list.insert(END, f"{name} ({age})")
                    else:
                        print(f"Skipping line due to incorrect format: {line.strip()}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def load_selected_data(self, event):
        selected_index = self.list.curselection()
    
        selected_index = int(selected_index[0])
        selected_text = self.list.get(selected_index)
        parts = selected_text.split(" ")
        if len(parts) == 2:
            name, age = parts[0].strip(), parts[1].strip()[1:-1]  
            self.name.set(name)
            self.age.set(age)

            search_term = self.search_entry.get()
            if self.selected.get() == 1:
                filename = "students.txt"
            elif self.selected.get() == 2:
                filename = "teachers.txt"
            else:
                return
            try:
                with open(filename, "r") as f:
                    for line in f:
                        parts = line.strip().split(",")
                        if len(parts) == 3:
                            _uuid, name, age = parts
                            if f"{name} ({age})" == selected_text:
                                self.uuid = _uuid
                                break
            except FileNotFoundError:
                print(f"File '{filename}' not found.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        self.delete_button.config(state=NORMAL)



    def delete_data(self):
        if not self.uuid:
            return

        if self.selected.get() == 1:
            filename = "students.txt"
        elif self.selected.get() == 2:
            filename = "teachers.txt"
        else:
            return

        LB_list = []

        try:
            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:  
                        _uuid, name, age = parts
                        if _uuid != self.uuid:
                            LB_list.append((_uuid, name, age))

            with open(filename, "w") as f:
                for _uuid, name, age in LB_list:
                    f.write(f"{_uuid},{name},{age}\n")

            self.clear_input_fields()
            self.update_Listbox()
            

        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def clear_input_fields(self):
        print("cif")
        self.name.set("")
        self.age.set("")
        self.uuid = None
        self.delete_button.config(state=DISABLED)

if __name__ == "__main__":
    window = Tk()
    app = SMA(window)
    window.mainloop()
