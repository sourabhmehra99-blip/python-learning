
def add_tasks():
    task = input("Enter your tasks: ")
    with open("Task","a") as file:
        file.write(task + "\n")
    print("Tasks added succesfully !!!")

def view_tasks():
    with open("Task","r") as file:
        task = file.readlines()
        if task:
            print("\n---your tasks---")
            for index,task in enumerate(task,start=1):
                print(f"{index}.{task}")
        else:
            print("NO task found!!")

def com_task():
        task = input("Enter task that completed: ")
        with open("Task","+a") as file:
         if task :
            print("\n---your task---")
            file.write(task + " @")
         else:
            print("Task not found")

def delete_task():
    with open("Task","w") as file:
        file.write("")

    print("all task deleted!!")

def main_menu():
    print("\n---To-Do List Menu---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. completed Task")
    print("4. Exit")

while True:
    main_menu()

    choice = int(input("Enter your choice(1-4): "))
    if choice == 1:
        add_tasks()

    elif choice == 2:
        view_tasks()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        com_task()
    else:
        print("Invalid statement\nTry again!!!")
