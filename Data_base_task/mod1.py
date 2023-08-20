class Student():
    def __init__(self, name, age) -> None:
        self.name= name
        self.age= age

    def write_name(self):
        print(f"my name is {self.name}")


std1= Student(name="Hopa",age=102)
std1.write_name()