# Filter only negative and zero in the list using list comprehension

# numbers = [-4, -3, -2, -1, 0, 2, 4, 6, 7, 8,]

# lst = [i for i in numbers if i>0 ]
# print(lst)

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [number for row in list_of_lists for number in row]


print(type(new_list))
print(new_list)
# output 
# <class 'list'>
# [1, 2, 3, 4, 5, 6, 7, 8, 9]