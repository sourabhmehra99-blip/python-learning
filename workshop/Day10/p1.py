# def fact(n):
#     if n ==1:
#         return 1
#     return n*fact(n-1)

# ans = fact(4)
# print(ans)

def sum(n):
    if n == 1:
        return 1
    return n+sum(n-1)

print(sum(5))

