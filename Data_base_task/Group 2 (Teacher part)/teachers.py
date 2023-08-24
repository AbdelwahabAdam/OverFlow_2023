# Teacher mangment system class

class Teachers:
    def __init__(self):
        self.teachers = []

    # Adding new teacher
    def add_teacher(self, name, age, hour_rate, english_teacher=False, math_teacher=False):
        teacher = {
            "name": name,
            "age": age,
            "hour_rate": hour_rate,
            "classes_given": [],
            "english_teacher": english_teacher,
            "math_teacher": math_teacher
        }
        # Appending to the main array(database)
        self.teachers.append(teacher)

    # listing method
    def list_teachers(self):
        for teacher in self.teachers:
            print(f" - Name: {teacher['name']} , Age: {teacher['age']} , Hourly Rate: {teacher['hour_rate']} , English Teacher: {teacher['english_teacher']} , Math Teacher: {teacher['math_teacher']}\n")

    # Search method
    def search_teacher(self, name=None, english_teacher=None, math_teacher=None):
        results = []

        for teacher in self.teachers:
            if  (name is None or name == teacher['name']) and \
                (english_teacher is None or english_teacher == teacher['english_teacher']) and \
                (math_teacher is None or math_teacher == teacher['math_teacher']):
                    results.append(teacher)
        return results

    # Delete method
    def delete_teacher(self, teacher):
        self.teachers.remove(teacher)

    # Update method
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

    # Bonus method
    def give_bonus(self, teacher_tb ,bonus):
        index = self.teachers.index(teacher_tb)
        teacher = self.teachers[index]
        teacher["hour_rate"] += bonus

    # Adding new session 
    def add_new_class(self, teacher, class_date):
        teacher['classes_given'].append(class_date)

    # Checking teacher classes
    def list_classes_given(self, teacher):
        return teacher['classes_given']

    # Checking month salary of the teacher
    def month_salary(self, teacher):
        return teacher['hour_rate'] * len(teacher['classes_given'])

