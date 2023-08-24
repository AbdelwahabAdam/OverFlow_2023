<details>
<summary>Click to toggle task details</summary>


### Problem Statement: Write a program to build a simple Teachers Management System using Python which can perform the following operations:

- Add
- List
- Search
- Delete
- Update
- give_raise
- list_number_of_classes_given
- month_salary
- add_new_class

----
## NOTES
- The task **must** be done using OOP
- The class name must be "Teacher"
- Each Teacher must have:
  - name: str
  - age: int
  - houre_rate: float
  - number_of_classes_given: list[date]
  - english_teacher: bool
  - math_teacher: bool
- we can add new Teacher
- we can List all Teacher 
- we can Search Teacher by only name or english_teacher  or math_teacher
- we can Delete a Teacher
- we can update a Teacher data
- we can give a all english or math teachers a bounce
- we can check how many class a certain teacher give
- we can check what is the salery a certain teacher will get

</details>

# Using

Create a virtual environment:
```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS and Linux:
```zsh
source venv/bin/activate
```
Install the required libraries:
```bash
pip install -r requirements.txt
```

Run the main script:
```bash
python main.py
```
Follow the on-screen instructions to interact with the Teacher Management System.