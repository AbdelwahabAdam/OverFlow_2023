class TeacherManagementSystem:
    def __init__(self):
        self.teachers = []

    def add_teacher(self, name, age, hour_rate, english_teacher=False, math_teacher=False):
        teacher = {
            "name": name,
            "age": age,
            "hour_rate": hour_rate,
            "number_of_classes_given": [],
            "english_teacher": english_teacher,
            "math_teacher": math_teacher
        }
        self.teachers.append(teacher)

    def list_teachers(self):
        for teacher in self.teachers:
            print(f"Name: {teacher['name']}, Age: {teacher['age']}, Hourly Rate: {teacher['hour_rate']}, English Teacher: {teacher['english_teacher']}, Math Teacher: {teacher['math_teacher']}")

    def search_teacher(self, name=None, english_teacher=None, math_teacher=None):
        results = []
        for teacher in self.teachers:
            if (name is None or name == teacher['name']) and \
               (english_teacher is None or english_teacher == teacher['english_teacher']) and \
               (math_teacher is None or math_teacher == teacher['math_teacher']):
                results.append(teacher)
        return results

    def delete_teacher(self, teacher):
        self.teachers.remove(teacher)

    def update_teacher(self, old_teacher, name=None, age=None, hour_rate=None, english_teacher=None, math_teacher=None):
        index = self.teachers.index(old_teacher)
        teacher = self.teachers[index]
        if name:
            teacher['name'] = name
        if age:
            teacher['age'] = age
        if hour_rate:
            teacher['hour_rate'] = hour_rate
        if english_teacher is not None:
            teacher['english_teacher'] = english_teacher
        if math_teacher is not None:
            teacher['math_teacher'] = math_teacher

    def give_bonus(self, teacher_tb ,bonus):
        index = self.teachers.index(teacher_tb)
        teacher = self.teachers[index]
        teacher["hour_rate"] += bonus

    def add_new_class(self, teacher, class_date):
        teacher['number_of_classes_given'].append(class_date)

    def list_number_of_classes_given(self, teacher):
        return len(teacher['number_of_classes_given'])

    def month_salary(self, teacher):
        return teacher['hour_rate'] * len(teacher['number_of_classes_given'])


if __name__ == "__main__":
    tms = TeacherManagementSystem()

    tms.add_teacher("John", 30, 20.0, english_teacher=True)
    tms.add_teacher("Emily", 28, 18.0, math_teacher=True)

    tms.list_teachers()
    teachers_to_update = tms.search_teacher(name="John")
    
    if teachers_to_update:
        
        teacher_to_update = teachers_to_update[0] # first teacher found
        tms.update_teacher(teacher_to_update, age=31, english_teacher=False)
        print("\nTeacher updated successfully!")

        print("\nTeachers after update:")
        tms.list_teachers()
    else:
        print("\nTeacher not found.")
    print("\n before bonus:")
    tms.list_teachers()

    tms.give_bonus(teachers_to_update[0],2.0)
    print("\n after bonus")
    tms.list_teachers()

    tms.add_new_class(teachers_to_update[0], "27/8/2023")
    tms.add_new_class(teachers_to_update[0], "28/8/2023")
    print(tms.list_number_of_classes_given(teachers_to_update[0]))
    tms.delete_teacher(teachers_to_update[0])
    tms.list_teachers()

