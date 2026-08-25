# Contact book 

# step 1 Initalize an empty contact book
contact_book = {}

# step 2 Display the menu options

def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Search Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email:")
    contact_book[name] = {"phone": phone,"email": email}
    print(f"{name} Contact added successfully!")

def view_contacts():
    if contact_book:
        print("\n---Contact List---")
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
    else:
        print("No contacts found.")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in contact_book:
        print(f"\n---Contact Details for {name}---")
        print(f"Name: {name}")
        print(f"phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
    else:
        print(f"{name} not found in contact book.")

def edit_contact():
    name = input("Enter contact name to edit: ")
    if name in contact_book:
        print(f"\n---Editing Contact: {name}---")
        new_phone = input("Enter new phone number (leave blank to keep current): ")
        new_email = input("Enter new email (leave blank to keep current): ")
        if new_phone:
            contact_book[name]['phone'] = new_phone
        if new_email:
            contact_book[name]['email'] = new_email
        print(f"{name} contact updated successfully!")
    else:
        print(f"{name} not found in contact book.") 

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"{name} contact deleted successfully!")
    else:
        print(f"{name} not found in contact book.") 

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
