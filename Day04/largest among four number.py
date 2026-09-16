# # program to find largest among four number:
# a, b, c, d = map(int, input("Enter four numbers: ").split())
# print(a, b, c, d)
a, b, c, d = map(int, input("Enter four number: ").split())
print(a, b, c, d)

if(a>b and a>c and a>d):
    print(f"{a} is greater.")
elif(b>c and b>d):
    print(f"{b} is greater.")
elif(c>d):
    print(f"{c} is greater.")
elif(a==b or a==c or a==d or b==c or b==d or c==d ):
    print(f"{a,b,c,d} some numbers are equal.")
else:
    print(f"{d} is greater.")
