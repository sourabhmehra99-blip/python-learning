# Python - Reduce Function
# The reduce() function is defined in the functools module and we should import it from this module.
#  Like map and filter it takes two parameters, a function and an iterable.
#  However, it does not return another iterable, instead it returns a single value.

from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
