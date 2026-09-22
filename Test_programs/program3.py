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

# the main file contain the sub dictinary 
student = {}
# add student function
def add_fun():
  name = input("Enter the name : ")
  if name in student: 
    print("student name already in details")

  else:
    student["Name"] = name
    student["Roll number"] = input("Enter the roll number : ")
    student["CGPA "] = float(input("Enter you cgpa"))

add_fun()


def view_fun():
   print("---Student Details---")

   for key, value in student.items():
    print( key,":",value)

   print ("===done===")

view_fun()

def search_fun():
  name = input("Enter the name to search : ")
  if name in student:
    print(f"---student details---")
    print(f"Name:{student(name)}")
    print(f"Roll Number:{student["Roll number"]}")
    print(f"CGPA :{student['CGPA']}")

  else:
      print("Name not found\n")

search_fun()

