#  password system 
def system():

    user = input("Enter the username: ")
    if user == "admin":
        while True:
            password = input("Enter the password: ")
            if password == "admin123":
                print("Welcome to the system")
                break
            else:
                print("Incorrect password. Please try again.")
    else:
        print("Access denied. Invalid username.")
        system()

system()
