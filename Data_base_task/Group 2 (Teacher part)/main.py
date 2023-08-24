from pick import pick
from termcolor import colored
import os
from teachers import Teachers

def add_teacher_ui(tms):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    hour_rate = float(input("Enter hourly rate: "))
    english_teacher = input("Is English teacher (y/n): ").lower() == "y"
    math_teacher = input("Is Math teacher (y/n): ").lower() == "y"
    tms.add_teacher(name, age, hour_rate, english_teacher, math_teacher)
    print("Teacher added successfully!")

def list_teachers_ui(tms):
    tms.list_teachers()

def search_teacher_ui(tms):
    name = input("Enter name (leave empty for any): ")
    english_teacher_input = input("Is English teacher (y/n/any): ")
    math_teacher_input = input("Is Math teacher (y/n/any): ")

    if english_teacher_input == "y":
        english_teacher = True
    elif english_teacher_input == "n":
        english_teacher = False
    else:
        english_teacher = None

    if math_teacher_input == "y":
        math_teacher = True
    elif math_teacher_input == "n":
        math_teacher = False
    else:
        math_teacher = None

    results = tms.search_teacher(name if name else None, english_teacher if english_teacher else None, math_teacher)
    print("Search results:")
    for teacher in results:
        print(f" - Name: {teacher['name']} , Age: {teacher['age']} , Hourly Rate: {teacher['hour_rate']}")

def update_teacher_ui(tms):
    name = input("Enter name of teacher to update: ")
    teachers_to_update = tms.search_teacher(name=name)
    if teachers_to_update:
        teacher_to_update = teachers_to_update[0]
        new_age = int(input("Enter new age: "))
        new_math_teacher = input("Is Math teacher (y/n): ").lower() == "y"
        new_english_teacher = input("Is English teacher (y/n): ").lower() == "y"
        tms.update_teacher(teacher_to_update, age=new_age, math_teacher=new_math_teacher, english_teacher=new_english_teacher)
        print("Teacher updated successfully!")
    else:
        print("Teacher not found.")

def give_bonus_ui(tms):
    name = input("Enter name of teacher to give bonus: ")
    teachers_to_bonus = tms.search_teacher(name=name)
    if teachers_to_bonus:
        bonus_amount = float(input("Enter bonus amount: "))
        tms.give_bonus(teachers_to_bonus[0], bonus_amount)
        print("Bonus given successfully!")
    else:
        print("Teacher not found.")

def add_class_ui(tms):
    name = input("Enter name of teacher to add class: ")
    teachers_to_add_class = tms.search_teacher(name=name)
    if teachers_to_add_class:
        class_date = input("Enter class date: ")
        tms.add_new_class(teachers_to_add_class[0], class_date)
        print("Class added successfully!")
    else:
        print("Teacher not found.")

def delete_teacher_ui(tms):
    name = input("Enter name of teacher to delete: ")
    teachers_to_delete = tms.search_teacher(name=name)
    if teachers_to_delete:
        tms.delete_teacher(teachers_to_delete[0])
        print("Teacher deleted successfully!")
    else:
        print("Teacher not found.")

def list_number_of_classes_given_ui(tms):
    name = input("Enter name of teacher to list number of classes given: ")
    teachers_to_check = tms.search_teacher(name=name)
    if teachers_to_check:
        teacher_to_check = teachers_to_check[0]
        class_dates = tms.list_classes_given(teacher_to_check)
        classes_given = len(class_dates)
        print(f"{teacher_to_check['name']} has given {classes_given} classes on the following dates: {class_dates}.")
    else:
        print("Teacher not found.")

def month_salary_ui(tms):
    name = input("Enter name of teacher to calculate month salary: ")
    teachers_to_calculate = tms.search_teacher(name=name)
    if teachers_to_calculate:
        teacher_to_calculate = teachers_to_calculate[0]
        salary = tms.month_salary(teacher_to_calculate)
        print(f"{teacher_to_calculate['name']}'s month salary is: {salary}.")
    else:
        print("Teacher not found.")

def main():
    tms = Teachers()

    options = [
        ("Add Teacher", add_teacher_ui),
        ("List Teachers", list_teachers_ui),
        ("Search Teacher", search_teacher_ui),
        ("Update Teacher", update_teacher_ui),
        ("Give Bonus", give_bonus_ui),
        ("Add Class", add_class_ui),
        ("Classes Given", list_number_of_classes_given_ui), 
        ("Calculate  Salary", month_salary_ui), 
        ("Delete Teacher", delete_teacher_ui),
        ("Exit", None)
    ]

    while True:
        title = "Teacher Management System"
        option_names = [option[0] for option in options]
        selected_option, _ = pick(option_names, title)

        selected_function = None
        for option in options:
            if option[0] == selected_option:
                selected_function = option[1]
                break

        if selected_function is None:
            print("Thank you for using!")
            break
        else:
            selected_function(tms)
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()