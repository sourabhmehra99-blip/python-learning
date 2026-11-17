# # list

# l1 = [10,20,30]
# print(l1)
# print(type(l1))

# l2 =[12,"jayesh",True,10.5]
# print(l2)

# l3 =[20,20,30,40,50,50]

# for i in l3:
#     print(i)

# print(l3[0])
# print(l3[1])

# list = [11,22,33,44,55]
    
# print(list)

# list.append(66) # append at the end of the list
# print(list)

# list.insert(2,99) 
# list.insert(0,'number') # insert at a specific index
# print(list)
# for i in list0+
#     print(i)

# l1 =[10,20,30,40,50]

# # l1.append([11,22,33]) # append at the end of the list
# l1.extend([11,22,33]) # extend at the end of the list
# print(l1)

# list = ['priyanshu','jay','sachin','jayesh']

# x = list.pop() # remove the last element from the list
# print(list)
# # print(x)
# print(list.pop(0)) # remove the element at index 1
# print(list)

# list.remove('jayesh') # remove the first occurrence of the element
# print(list)

list = []

n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter element: "))
    list.append(element)

print(list)
n = int(input("Enter the number to check: "))
print(n in list) # check if 10 is in the list

