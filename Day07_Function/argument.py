# If we do not know the number of arguments we pass to our function
# we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

# syntax
# Declaring a function
# def function_name(*args):
#     codes
#     codes
# Calling function
# function_name(param1, param2, param3,..)

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10

