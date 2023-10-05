from tkinter import * 
class Database:
    def __init__(self, ob, type):
        valid_types = ['student_data', 'teacher']
        if type not in valid_types:
            raise ValueError(f"Invalid type. Allowed types: {', '.join(valid_types)}")
        self.ob = ob
        self.type = type

####################################################################

    def add_data(self):
        if self.selected.get() == 1:
            with open("Student_data.txt", "a") as f:
                f.write(f"{self.name.get()},{self.age.get()}\n")
        elif self.selected.get() == 2:
            with open("Teacher_data.txt","a") as f:
                f.write(f"{self.name.get()},{self.age.get()}\n")

####################################################################
                
    def list_data(self):
        file1 = open(f"{self.type}.txt","r")
        for i in file1.readlines():
            print(i)
        return file1.readlines()

####################################################################

    def search_data(self, value):
        with open(f"{self.type}.txt", 'r') as file:
            for line in file:
                if value in line:
                    print(line)

####################################################################
    def delete_data(self, value, flag=1): ##flag = 1,ALL
        x = flag
        with open(f"{self.type}.txt", 'r') as file:
            lines = file.readlines()
        
        if x == 'ALL':
            with open(f"{self.type}.txt", 'w') as file:
                for line in lines:
                        if value not in line:
                            file.write(line)
        else:
            with open(f"{self.type}.txt", 'w') as file:
                for line in lines:
                        if x != 0:
                            if value in line:
                                x-=1
                            else:
                                file.write(line)
                        else:
                            file.write(line)
        print(print(f"{self.type} data was deleted successfully"))
#############################################################
def update_data(self):
    pass

### HOW TO USE
# from student import Student

## Add data
# std = Student(name= "hopa", age= 45 , height= 5.0 , 
#             class_name= 'A1', english_score= 0.0,
#             math_score= 150.2, attendance_score= 4.2, 
#             gpa = 4.4) 
# db = Database(ob=std, type='student')
# db.add_data()

## Search data
# db = Database(ob=Student, type='student')
# db.search_data(value='45') ## any value from the object attr

## Delete data
# db = Database(ob=Student, type='student')
# db.delete_data(value='hopa', flag=1)
