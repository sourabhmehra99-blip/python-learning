
students = [] #list to store student records

def add_fun():
    name = input("Enter student name: ")
    roll = int(input("Enter Roll number: "))
    cgpa = float(input("Enter Cgpa: "))
    students.append({"Name":name, "roll":roll, "cgpa":cgpa})
    print("✅ Student added successfully!\n")

def view_fun():
    if not students:
        print("No student found!\n")
    else:
        print("--- Student List ---")
        for s in students:
            print(f"Name:{s['Name']}\nRoll number: {s['roll']}\nCgpa: {s['cgpa']}\n")
        print()

def search_fun():
    roll = int(input("Enter roll number to search: "))
    for s in students:
        if s['roll'] == roll:
             print(f"Name:{s['Name']}\nRoll number: {s['roll']}\nCgpa: {s['cgpa']}\n")
        else:
             print("No student found!\n")

def find_topper():
    if not students:
        print("No student found")
    else:
        topper = max(students,key=lambda x:x['cgpa'])
        print(f"Topper\n Name: {topper['name']}\nRoll number: {topper['roll']}\nCgpa: {topper['cgpa']}\n")

def cal_average():
    if not students:
        print("No student found")
    else:
        avg = sum(s["cgpa"]for s in students)/len(students)
        print(f"📊 Average Marks: {avg:.2f}\n")

def del_fun():
    roll = int(input("Enter the roll number: "))
    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            print("🗑️ Student deleted successfully!\n")
            return
    print("❌ Student not found!\n")

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
            find_topper()
        elif choice == 5:
            cal_average()
        elif choice == 6:
            del_fun()
        elif choice == 7:
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

menu()