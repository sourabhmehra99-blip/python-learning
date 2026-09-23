# diamond or kaju katli pattern

row = int(input("Enter the number of rows : "))

for x in range(1,row + 1):
    for y in range(1,row -x+1):
        print(" ",end="")
    for y in range(1,2*x):
        print("*",end="")

    print()

for x in range(row,0,-1):
    for y in range(1,row -x+1):
        print(" ",end="")
    for y in range(1,2*x):
        print("*",end="")

    print()

# Enter the number of rows : 5
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *