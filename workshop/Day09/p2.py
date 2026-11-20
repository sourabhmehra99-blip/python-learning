# function two types
# use for reuseablity
# avoid code duplication

# first without parameter without return type
def sum():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a + b
    print("Sum is:", c)

sum() # Sum is: 30

# without parameter with return type
def sum():
    a = int(input("Enter first number: ")) # 10
    b = int(input("Enter second number: ")) # 20
    
    return a + b

print(sum()) # 30

# with parameter without return type

def sum(a,b):
    c = a+b
    print("Sum is:", c)

a = int(input("Enter first number: ")) # 10
b = int(input("Enter second number: ")) # 20    
sum(a,b)

# with parameter with return type

def sum(a,b):
    return a+b

a = int(input("Enter first number: ")) # 10
b = int(input("Enter second number: ")) # 20
print(sum(a,b))

def add(a,b):
    print(a+b)

add(11,22,11) # add() takes 2 positional arguments but 3 were given

# default arguments

def add(a=0,b=0,c=0):
    print(a+b+c)

# add(2,4,5,6) # gives error
add(1,2,3)
add (2,3)
add(5)
add()

def show(name="user",n =3):
    for i in range(n):
        print("Hello",name)
    print()

show("sumit")

def display(name="user",roll = 00,marks = 0.00):
    print("Name:",name)
    print("Roll:",roll)
    print("Marks:",marks)
    print()

display("sumit",101,90.5)

def display(name="user",roll = 00,marks = 0.00):
    print("Name:",name)
    print("Roll:",roll)
    print("Marks:",marks)
    print()

# display("sumit",marks = 89,146) # give error because positional argument follows keyword argument
display("sumit",marks = 89,roll =146) 

# Menu driven program

def sum(a,b):
    c = a+b
    print("Sum is:", c)

def sub(a,b):
    c = a-b
    print("Sum is:", c)

def mult(a,b):
    c = a*b
    print("Mult is:", c)

def divi(a,b):
    c = a/b
    print("Div is:", c)



while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter first number: ")) # 10
        b = int(input("Enter second number: ")) # 20    
        sum(a,b)
    elif choice == 2:
        a = int(input("Enter first number: ")) # 10
        b = int(input("Enter second number: ")) # 20    
        sub(a,b)
    elif choice == 3:
        a = int(input("Enter first number: ")) # 10
        b = int(input("Enter second number: ")) # 20    
        mult(a,b)
    elif choice == 4:
        a = int(input("Enter first number: ")) # 10
        b = int(input("Enter second number: ")) # 20    
        divi(a,b)
    elif choice == 5:
        break
    else:
        print("Invalid choice")

# even odd number using function
# grades calculation 
# user age voting eligibility or not 