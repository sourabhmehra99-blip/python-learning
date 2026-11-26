# list Comprehension

l1 = [1, 2, 3, 4, 5,]

d1 = {l1.index(i)+1: i for i in l1}
print(d1)

l2 = [1, 2, 3, 4, 5]

d2 = {i : "Even" if i%2==0 else "Odd" for i in l2}
print(l2)
# print(d2)

roll = [11,22,33,44,55]
name =["Ravi", "Ramesh", "Suresh", "Mahesh", "Rajesh"]

student = {roll[i]: name[i] for i in range(len(roll))}
print(student)
