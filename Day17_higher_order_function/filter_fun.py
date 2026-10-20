# Python - Filter Function
# The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.

#     # syntax
#     filter(function, iterable)

# Lets filter only even numbers
numbers = [1, 2, 3, 4, 5,6]  # iterable

def is_even(num):
    if num % 2==0:
        return True
    return False

# even_number = map(is_even,numbers)
# print(list(even_number))   output <- [False, True, False, True, False, True]

even_number = filter(is_even,numbers)
print(list(even_number)) # output <- [2, 4, 6]


# let filter only odd numbers

numbers = [1, 2, 3, 4, 5, 6]  # iterable

def odd_num(num):
    if num %2 != 0:
        return True
    return False
odd_number = list(filter(odd_num,numbers))
print(odd_number)

# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def long_name(name):
    if len(name) > 7:
        return True
    return False

new_name =list(filter(long_name,names))
print(new_name)


