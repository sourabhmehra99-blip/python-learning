# reverse of a number


num = int(input("Enter the number: "))
rem = 1
rev = 0
while num !=0:
    rem = num % 10 
    rev = (rev * 10) + rem
    num = num // 10

print(f"the reverse number : {rev}")

# palindrome number

num = int(input("Enter the number: "))
temp = num
rem = 1
rev = 0
while num !=0:
    rem = num % 10
    rev =(rev * 10 ) + rem
    num = num // 10

if temp == rev:
    print(f"{temp} is a palindrome number...")
else:
    print(f"{temp} is not a palindrome number...")