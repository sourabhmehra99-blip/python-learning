# # bitwise operations

a = 5
b = 3
print(a & b)  # bitwise AND
print(a | b)  # bitwise OR
print(a ^ b)  # bitwise XOR
print(~a)     # bitwise NOT
print(a << 1)  # left shift
print(a >> 1)  # right shift

# # output:
# # 1
# # 7
# # 6
# # -6
# # 10
# # 2

# Membership operators - in ,not in

name = "souarbh"
print('s' in name)  # True
print('z' not in name)  # True
print('t' in name)  # False

# Identity operators - is , is not
x = 10
y = 20

print(x is y)   # False
print(x is not y)   # True
print(id(x))  # prints the memory address of x
