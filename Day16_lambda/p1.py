# # syntax
# x = lambda param1, param2, param3: param1 + param2 + param3
# print(x(arg1, arg2, arg3))

# basic lambda function code

add_nums = lambda a,b,c: a+b+c
print(add_nums(4,2,4))

square = lambda n: n**2
print(square(4))

number = [1,2,3,4,5,6]

even_num = list(filter(lambda x:x%6 ==0,number))
print(even_num)

students = [
    ("kumal",86),
    ("aman",77),
    ("neha",91)
]
students.sort(key=lambda x:x[1])
print(students)

def power(x):
    return lambda n:x **n

print(power(2)(3))
