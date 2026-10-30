# if else statement

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("Negative")

# age
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# marks

marks = int(input("Enter your marks: "))
if marks >= 50:
    print("You have passed.")
else:
    print("You have failed.")

# even odd 
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

a,b,c = map(int, input("Enter three number: ").split())
if a == b ==c:
    print("All are equal")
else:
    if a>b:
        if a>c:
            print(a ,"is greater")
        else:
            print(c ,"is greater")
    else:
        if b>c:
            print(b,"greater")
        else:
            print(c,"greater")

# student marks 

marks = int(input("Enter your marks: "))
if marks >0 and marks <= 100:
    if marks >= 90:
        print("Grade: A\nyou are brilliant!")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F\nyou are worse than average!")
else:
    print("Invalid marks. Please enter a number between 0 and 100.")
