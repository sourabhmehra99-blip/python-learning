# Decreasing star pattern
row = int(input("Enter number of rows : "))

for x in range(row,0,-1):
    for y in range(x): # or (for y in range(1,x+1))
        print("*",end=" ")

    print()

# output 
# Enter number of rows : 5
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 