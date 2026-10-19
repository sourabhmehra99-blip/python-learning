# The map() function is a built-in function that takes a function and iterable as parameters.

#     # syntax
#     map(function, iterable)

number =[1,2,3,4,5]

def square(x):
    return x**2

lst = map(square,number)
print(lst) # this will not print the output lsit is important 
print(list(lst))

numbers_str = [1,2,3,4,5,6]  # iterable
numbers_int = map(tuple, numbers_str)

print(numbers_int)
print(list(numbers_int))

number = list(map(int,input("Enter the number: ").split()))
print(number)

words = ["java","python","c++"]

alp = list(map(str.upper,words))
print(alp)

number =[1,2,3,4,5]

square = list(map(lambda x:x**2,number))
cude = list(map(lambda x: x**3,number))
print(square)
print(cude)