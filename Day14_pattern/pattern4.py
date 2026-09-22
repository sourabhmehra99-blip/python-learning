
# row = int(input("Enter number of rows : "))

# for x in range(1,row + 1):
#     for y in range(x):
#         print("*",end=" ")

#     print()

row = int(input("Enter number of rows : "))

for x in range(row,0,-1):
    for y in range(x):
        print("*",end=" ")

    print()