# i = 1

# while i<10:
#     print(i)
#     i+=1

# print("Exit value of i is ",i)

# table of a number

num = int(input("Enter the number: "))
i =1
while i<=50:
    print(f"{num} x {i} = {num*i}")
    if i%5 == 0:
        print("------------")
    i+=1