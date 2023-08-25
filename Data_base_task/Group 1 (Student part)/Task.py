q1 = int(input("enter the school capacity (in numbers please) : "))
v = 0
r = 1
while v < q1 :
    N = str(input(f"Enter student{r}'s name : ")).title().lower()
    A = int(input(f"Enter student{r}'s age : "))
    H = float(input(f"Enter student{r}'s hight : "))
    C_A = str(input(f"Enter student{r}'s class name : ")).title().lower()
    E_S = float(input(f"Enter student{r}'s English score : "))
    M_S = float(input(f"Enter student{r}'s Math score : "))
    A_S = float(input(f"Enter student{r}'s Attendance score : "))
    G = float(input(f"Enter student{r}'s gpa : "))
    s_y = int(input(f"Enter student{r}'s grade : "))
    f_l = {N : {}}
    f_l[N].update({"name": N , "age" : A , "hieght" : H , "class_name" : C_A , "English score" : E_S , "Math score" : M_S , "Attendance score" : A_S , "gpa" : G , "grade" : s_y})
    print("-_" * 80)
    r += 1
    v += 1
class student :
    def _init_(self,name,age,hight,class_name,english_score,math_score,attendance_score,gpa,grade) :
        self.name = name
        self.age = age
        self.hight = hight
        self.class_name = class_name
        self.english_score = english_score
        self.math_score = math_score
        self.attendance_score = attendance_score
        self.gpa = gpa
        self.grade = grade
    def add_students(self) :
          h = 1
          f = 0
          q5 = str(input("do you want to add student write (yes) or (no) : ")).lower().strip()
          if q5 == "yes" :
                q6 = int(input("how many students do you want to add : "))
                while f < q6 :
                    N = str(input(f"Enter student{h}'s name : ")).title().lower()
                    A = int(input(f"Enter student{h}'s age : "))
                    H = float(input(f"Enter student{h}'s hight : "))
                    C_A = str(input(f"Enter student{h}'s class name : ")).title().lower()
                    E_S = float(input(f"Enter student{h}'s English score : "))
                    M_S = float(input(f"Enter student{h}'s Math score : "))
                    A_S = float(input(f"Enter student{h}'s Attendance score : "))
                    G = float(input(f"Enter student{h}'s gpa : "))
                    s_y = int(input(f"Enter student{h}'s grade : "))
                    v_l = {N : {}}
                    v_l [N].update({"name": N , "age" : A , "hieght" : H , "class_name" : C_A , "English score" : E_S , "Math score" : M_S , "Attendance score" : A_S , "gpa" : G , "grade" : s_y})
                    f_l.update(v_l)
                    print("-_" * 80)
                    h += 1
                    f += 1
          elif q5 == "no" :
              print("ok , let's go to next option ")
              q0 = input("press 'ENTER'")
    def old_new_student(self) :
        q70 = str(input("do you want to know if the student old or new write (yes) or (no) : ")).lower().strip()
        if q70 == "yes" :
          q30 = input("enter the student name : ").lower().strip()
          if f_l[q30,s_y] > 10 :
            print("this's old student : ")
            print("ok , let's go to next option ")
            input("press ENTER")
        elif f_l[q30,s_y] < 10 :
            print("this's new student : ")
            print("ok , let's go to next option ")
            input("press ENTER")
    def update_student_data(self) :
        p = 0
        v =0 
        j = 1
        q11 = str(input("do you want to add student write (yes) or (no) : ")).lower().strip()
        if q11 == "yes" :
            q15 = int(input("how many student do you want to change his\\her information : "))
            while v < q15 :
                q12 = str(input(f"what's the student{j}'s name : ")).lower().strip()
                q13 = int(input("how many thing do you want to change (in numbers please) : "))
                while p < q13 :
                    q7 = str(input("what is the thing you want to update (#NOTE# : write its name 'EX' : name 'or' age etc... ) ")).lower().strip()
                    q14 = input(f"what is the new {q7}")
                    f_l[q12].clear({q13})
                    f_l[q12].update({q7 : q14})
                    p += 1
                j += 1
                v += 1
        elif q11 == "no" :
            print("ok , let's go to next option ") 
    def call_student(self) :
        q2 = str(input("do you want to call any student write (yes) or (no) : ")).lower().strip()
        if q2 == "yes" :
            q3 = str(input("enter the student you want to call name : ")).lower().strip()
            print(f_l[q3])
        elif q2 == "no" :
            print("ok , let's go to next option ")
            q4 = input("press 'ENTER'")
            print(f"-_{q4}" * 80)
    def remove_student(self) :
        z = 0
        y =0 
        sh = 1
        q11 = str(input("do you want to remove student write (yes) or (no) : ")).lower().strip()
        if q11 == "yes" :
            q15 = int(input("how many student do you want to remove his\\her information : "))
            while z < q15 :
                q12 = str(input(f"what's the student{sh}'s name : ")).lower().strip()
                f_l.clear([q12])
                sh += 1
                z += 1
s = student(name = N,age = A,hight = H,class_name = C_A,english_score = E_S,math_score = M_S,attendance_score = A_S,gpa = G,grade = s_y)
s.add_students()
s.old_new_student()
s.update_student_data()
s.call_student()
s.remove_student()