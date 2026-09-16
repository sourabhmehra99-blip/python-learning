# Input while creating an object

class student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def std_details(self):
        print(f"student name is {self.name} in class {self.grade}")

name = input("Enter the name: ")
grade = input("Enter the grade: ")

student1 = student(name,grade)

student1.std_details()

# Here the flow is:

# input()
   ↓
# variables
   ↓
# Student(name, age)
   ↓
# __init__()
   ↓
# self.name / self.age
