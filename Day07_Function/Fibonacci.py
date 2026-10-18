"""
    Calculates the n-th Fibonacci number using recursion.
    Base cases:
    - F(0) = 0
    - F(1) = 1
    For n > 1:
    - F(n) = F(n-1) + F(n-2)
    """

def fab(n):
    if n == 0 or n==1:
       return 1
    else:
       return fab(n-1)+fab(n-2)

num = int(input("Enter the number: "))

for x in range(num):
   print(fab(x))