# Tuple
t1 = (1, 2, 3, 4, 5)
print(t1)
print(type(t1))

t2 = 33,"rutn",99.99
print(type(t2))
print(t2)

t3 =(10)
print(type(t3)) # int

t4 =(10,20,30,40,50,60,70,80,90,100)

print(t4.index(30)) # postion of value in tuple
print(t4[2]) # accessing value in tuple

# packing

roll = 146
name = "rahul"
marks = 99.99
tuple = roll,name,marks
print(type(tuple))
print(tuple)

# unpacking

t4 = (10,20,30)
n1, n2, n3 = t4
print(n1)
print(n2)
print(n3)   
print(type(n1))

t1 = (1,2,3,4,5,6,7,8,9,10)
a,b,*c = t1  # *c captures the remaining elements as a list
print(a)     # 1
print(b)     # 2
print(c)     # [3, 4, 5, 6, 7, 8, 9, 10]

# Nested list for n number of students records roll number, name, marks 
# opreation insert ,search, delete, update, display
