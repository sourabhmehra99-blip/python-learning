# Right angle triangle pattern

rows =int(input("Enter no of rows: "))

# Outer loop
for x in range(1,rows + 1):
    
        for y in range(rows-x):
                print(" ",end="")
        for y in range(x):
                print("* ",end="")
        print()
    