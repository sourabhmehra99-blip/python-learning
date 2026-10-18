
students = [] # make the main list to store the students data

def add_fun():
    name = input("Enter student name: ")
    if name in students:
        print("Student already in student list!!")
    else:
        age = int(input("Enter student age: "))
        roll = int(input("Enter student roll number: "))
        cgpa = float(input("Enter current Cgpa: "))
        students.append({"Name":name,"age":age,"roll":roll,"cgpa":cgpa})
        print("studnet added succesfully")

def view_fun():
    if not students:
        print("No student found!")
    else:
        print("---student list---")
        for s in students:
            print(f"Name:{s['Name']}\nage:{s['age']}\nroll number:{s['roll']}\ncgpa:{s['cgpa']}")
            print("---studnet details---")

def search_fun():
    roll = int(input("Enter roll number to search: "))
    for s in students:
        if s['roll'] == roll:
            print(f"Name:{s['Name']}\nage:{s['age']}\nroll number:{s['roll']}\ncgpa:{s['cgpa']}")
        else:
            print("students found")

def topper_fun():
    if  not students:
        print("no student in list")
    else:
        topper = max(students,key=lambda x:x['cgpa'])
        print(f"Topper\n Name: {topper['name']}\nRoll number: {topper['roll']}\nCgpa: {topper['cgpa']}")

def menu():
    while True:
        print("================================")
        print("     STUDENT MANAGEMENT SYSTEM  ")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Find Topper")
        print("5. Calculate Average")
        print("6. Delete Student")
        print("7. Exit")
        
        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            add_fun()
        elif choice == 2:
            view_fun()
        elif choice == 3:
            search_fun()
        elif choice == 4:
            topper_fun()
        # elif choice == 5:
        #     cal_average()
        # elif choice == 6:
        #     del_fun()
        elif choice == 7:
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

menu()