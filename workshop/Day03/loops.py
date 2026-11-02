i = 1

while i<10:
    print(i)
    i+=1

print("Exit value of i is ",i)

# table of a number

num = int(input("Enter the number: "))
i =1
while i<=50:
    print(f"{num} x {i} = {num*i}")
    if i%5 == 0:
        print("------------")
    i+=1

for i in range(1,10,1):
    print(i)

for i in range(10,0,-1):
    print(i)

for i in reversed(range(1,10,2)):
    print(i)

# fibonacci series

n = int(input("Enter the number of terms: "))
f = 0
s = 1
print(f)
print(s)
for j in range(3,n+1):
    next = f +s
    print(next)
    f = s
    s = next
    
while n>2:
    next = f+s
    print(next)
    f = s
    s = next
    n-=1    
for i in range(1,20):
    if i%5 == 0:
        break

    if i % 5 == 0:
        continue

    if i%5 == 0:
        pass
    print(i)


