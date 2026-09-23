# a matric star pattern code

row = int(input("Enter number of rows : "))
col = int(input("Enter number of column : "))

for x in range(row):
    for y in range(col):
        print("* ",end="")

    print()