try:
    file = open("employee.txt","a") 
    data = file.read

# if the file not found this will give statement but program will not crash 
except FileNotFoundError:
    print("Employee file not found ")

# finally function always executes at any cost 

finally:
    print("File operstion completed")