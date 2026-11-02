# sum of natural numbers for n terms

num = int(input("Enter number : "))
sum = 0
for i in range(1,num+1):
    sum = sum +i

print(f"the sum of n term : {sum}")

# any other way to do this 
num = int(input("Enter number : "))
sum = (num*(num+1))/2
print(f"the sum of n term : {sum}")
