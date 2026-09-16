class Student:
    def __init__(self,name,age,grade,marks):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = marks

    def display(self):
        print("Name: ",self.name)
        print("age: ",self.age)
        print("Class: ",self.grade, "sem")
        print("Marks: ",self.marks)

name = input("Enter student name: ")
age = int(input("Enter student age :"))
grade = int(input("Enter current class :" ))
marks = float(input("Enter last class marks: "))
student1 = Student(name,age,grade,marks)

student1.display()
