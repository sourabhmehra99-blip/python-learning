# Palindrone number
try: 
   num = int(input("Enter the number: "))
   fir = num
   rev = 0 

   for x in range(len(str(num))):
    digits = num % 10
    rev = rev * 10 + digits
    num //= 10

   if fir == rev:
    print("the number is palindrome.")
   else:
    print("Not a palindrome.")
except:
    print("write only number")
