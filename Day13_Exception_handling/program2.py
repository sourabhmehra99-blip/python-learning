# login System 

correct_password = "python1234"

try:
    password = input("Enter the password to login : ")

    if password != correct_password:
        raise ValueError("Incorrect password\nLogin failed\tTry again")

    else:
        print("Login succesfully!")
except ValueError as error:
    print(error)