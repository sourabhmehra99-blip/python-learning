# variable and its types

print("hello world")

roll =46
print(type(roll))
print(roll)
name = "Sourabh"
# print("Name is ",name)
print(f"Name is {name}\nRoll number is {roll}")
print(type(name))
marks = 45.5
print(type(marks))

a = 44
print(type(a))
a ="hil"
print(type(a))
a = True
print(type(a))
print(a) 
print(a)
print(a) # only show the last value .

name = input("Enter name : ")
roll = int(input("Enter roll number : "))
cgpa = float(input("Enter cgpa : "))
print(f"Name : {name}\nRoll number : {roll}\nCgpa : {cgpa}")
print(type(name))
print(type(roll))
print(type(cgpa))

n1,n2,n3, = input("Enter three names : ").split(',')
print(f"Numbers are {n1}\n{n2}\n{n3}")

n1,n2,n3, = map(int,input("Enter three numbers : ").split())
print(f"Numbers are {n1}\n{n2}\n{n3}")

lambda function syantax
a = 4
b = 10
sum = lambda x,y : x+y
print(f"Sum of {a} and {b} is {sum(a,b)}")

a = 10 
b= 20 
c= a = b
print(c)

a = 10 
b= 20 
print(type(a))
c= a == b
print(c)
print(type(c))
