from database import Database

class Student():
    def __init__(self,name='',age=0,height=0,class_name='',english_score=0,math_score=0,attendance_score=0,gpa=0):
        self.name = name
        self.age = age
        self.height = height
        self.class_name = class_name
        self.english_score = english_score
        self.math_score = math_score
        self.attendance_score = attendance_score
        self.gpa = gpa
        
    def list_all(self):
        return [self.name, self.age, self.height, self.class_name, self.english_score, self.math_score, self.attendance_score, self.gpa]

    def add_Student(self):
        db = Database(type='student',ob=self)
        db.add_data()
        print(f"Student {self.name} has been added.")

    def search_student(self, value):
        db = Database(type='student',ob=self)
        print(f"search result is:")
        db.search_data(value=value)

    def delete_Student(self, value,flag=1):
        db = Database(type='student',ob=self)
        db.delete_data(value=value, flag=flag)
        print(f"Student with {value} has been deleted.")

    def update_Student(self, value1,value2):
        db = Database(type='student',ob=self)
        #db.update_data(value1=value1,value2=value2)
        print(f"Student with {value1} and {value2} has been updated.")

    def list_Students(self,):
        db = Database(type='student',ob=self)
        print(f"Listing all Student:")
        db.list_data()


# std = Student(name= "Ali", age= 10 , height= 5.0 , 
#             class_name= 'A1', english_score= 0.0,
#             math_score= 150.2, attendance_score= 4.2, 
#             gpa = 4.4)     
# std.add_Student()

# std2 = Student(name= "Hossam", age= 15 , height= 5.0 , 
#             class_name= 'A1', english_score= 0.0,
#             math_score= 150.2, attendance_score= 4.2, 
#             gpa = 4.4)     
# std2.add_Student()

# std3 = Student(name= "Hopa", age= 150 , height= 5.0 , 
#             class_name= 'A1', english_score= 0.0,
#             math_score= 150.2, attendance_score= 4.2, 
#             gpa = 4.4)     
# std3.add_Student()
# std3.list_Students()


Student().list_Students()
Student().search_student(value='Hopa')
Student().delete_Student(value='Hossam',flag=1)
Student(name= "Hopa_updated", age= 151 , height= 5.0 , 
            class_name= 'A1', english_score= 0.0,
            math_score= 150.2, attendance_score= 4.2, 
            gpa = 4.4).update_Student(value1='Hopa',value2='150')
