class Student():
    def __init__(self,name,age,height,class_name,english_score,math_score,attendance_score,gpa):
        self.name = name
        self.age = age
        self.height = height
        self.class_name = class_name
        self.english_score = english_score
        self.math_score = math_score
        self.attendance_score = attendance_score
        self.gpa = gpa
        
    def List_All(self):
        print("Name : ", self.name)
        print("Age : " , self.age)
        print("Height : ", self.height)
        print("class_name : ", self.class_name)
        print("english_score : ", self.english_score)
        print("math_score : ", self.math_score)
        print("attendance_score : ", self.attendance_score)
        print("gpa : ", self.gpa)
        print("\n")
        
        
    def Add_Student(self):
        self.name = input("Name : ")
        self.age = int(input("Age : "))
        self.height = float(input("Height : "))
        self.class_name = input("Class Name: ")
        self.english_score = float(input("English Score (/10): "))
        self.math_score = float(input("Math Score (/10): "))
        self.attendance_score = float(input("Attendance Score (/10): "))
        self.gpa = float(input("GPA (/5): "))
        
        Requirements = Student(self.name,self.age,self.height,self.class_name,
                               self.english_score,self.math_score,self.attendance_score,self.gpa)

        Students_List.append[Requirements]

    def Delete_Student(self)
        pass
    
std = Student(name= "", age= 0 , height= 0.0 , 
              class_name= '', english_score= 0.0,
              math_score= 0.0, attendance_score= 0.0, 
              gpa = 0.0)     
      
std_1 = Student(name = "Hossam", age = 16, height = 185.6 ,
                class_name='SpongeBob' , english_score=9.9 , 
                math_score= 8.3 , attendance_score=5.3 , 
                gpa= 4.7 )

std_2 = Student(name = "Anas", age = 15, height = 175.6 ,
                class_name='SpongeBob' , english_score=7.9 , 
                math_score= 9.2 , attendance_score=10.0 , 
                gpa= 5.0 )

std_3 = Student(name = "Galal", age = 11, height = 140.6 ,
                class_name='Donkey' , english_score=2.6 , 
                math_score= 3.2 , attendance_score=2.0 , 
                gpa= 1.3 )

Students_List = []  

std_1.List_All()

Student.Add_Student()

