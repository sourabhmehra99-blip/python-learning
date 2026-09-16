def menu():
    print("1.add notes")
    print('2.view notes')
    print('3.delete notes')

def add_notes():
    with open("notes.txt","a+") as file:
        note = input("Enter your note:")
        file.write(note + "\n")

def view_notes():
    with open("notes.txt","r") as file:
        notes = file.readlines()
        if notes:
            print("\n---Your Notes---")
            for note in notes:
                print(note.strip())
        else:
            print("No notes found.")

def delete_notes():
    with open("notes.txt","w") as file:
        file.write("")

while True:
    menu()
    choice = input("Enter your choice (1-3): ") 
    if choice == "1":  
        
        add_notes()

    elif choice == "2":
        view_notes()    

    elif choice == "3":
        delete_notes()
        print("All notes deleted successfully.")
    else:
        print("Invalid choice. Please try again.")# # note taking app


def main_menu():
    print("Welcome to the Note Taking App!")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Delete a note")
    print("4. Exit")

def add_notes():
    with open("notes.txt","+a") as file:
        note = input("Enter your task: ")
        file.write(note + "\n")
    print("Notes added succesfully! ")

def view_notes():
    with open("notes.txt","r") as file:
        note = file.readlines()
        if note:
            print("\n---Your Notes---")
            for index,note in enumerate(note,start =1):
                print(f"{index}.{note.strip()}")
        else:
            print("No notes found")
def delete_note():
    with open("notes.txt","w") as file:
        file.write("")
    print("all notes deleted! ")


while True:
    main_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_notes()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid statement!\nTry again")
