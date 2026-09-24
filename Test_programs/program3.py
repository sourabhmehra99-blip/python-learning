# 🚀 CHALLENGE 3 — STUDENT MANAGEMENT SYSTEM

def main_menu():
    print("""================================
     STUDENT MANAGEMENT SYSTEM
================================

1. Add Student
2. View Students
3. Search Student
4. Find Topper
5. Calculate Average
6. Delete Student
7. Exit""")

student = {}

def add_fun():
    student["Roll Number"] = int(input("Enter the roll number of student : "))
    student["Name"] = input("Enter the name of student : ")
    student["CGPA"] = float(input("Enter the currect cgpa : "))
    student["other details"] = input("Enter the any other details as required : ")

    print("Student details added succesfully")

def view_fun():
    if student:
        print("=== student details ===")
        for key ,value in student.items():
            print(key,":",value )

def search_fun():
    roll = int(input("Enter the roll number to search : "))

    for value in student.values():
        if value == roll:
            print("---details found---")
            view_fun()

def top_fun():
    find = int(input("Enter the requried cgpa value : "))
    
    for value in student.values():
        if value > find:
            print(f"found the students of same cgpa {find}")
            view_fun()

while True:
    main_menu()
    choice = int(input("Enter your choice (1-7): "))
    if choice == 1:
        add_fun()
    elif choice == 2:
        view_fun()
    elif choice == 3:
        search_fun()
    elif choice == 4:
        top_fun()
    else:
        print("Exit")
        break




search_fun()
view_fun()

        










