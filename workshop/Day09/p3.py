# # *args - multiple length positional arguments
# # * multiple positional arguments accept karta ha
# # argss - internally tuple hote ha

# def add(*args):
#     print(type(args)) # <class 'tuple'>
#     sum =0
#     for i in args:
#         sum += i
#         print("Addition is ",sum)

# add(1)
# add(4,6)
# add(10,20,30)

# def display(*details):
#     if (len(details)>=3):
#         print("Roll ",details[0])
#         print("name",details[1])
#         print("marks ",details[2])
#         print()

# display(12)
# display(12,"raj",33.4)
# display(12,"ayush")

# ** kwargs - multiple lenght keyword arguments
#    Kwargs - internally its dictionary 


# def data(**kwargs):
#     for i in kwargs.keys():
#     #   print(type(kwargs))
#      print(i," : ",kwargs[i])

# data(roll = 146,name = "sourabh",marks = 7.60)
# data(roll = 115,name = "priya",marks = 6.9)

# def add(**nums):
#     sum = 0
#     for i in nums.values():
#         sum +=i
#         # count += nums[i] 
#     print(sum)

# add(r=33)
# add(a=10,b = 20)
# add(a=11,b=22,c=33)
# add(a=44,b=55,c=66,d=87)

# def marks(**per):
#     sum = 0
#     for i in per:
#         sum += per[i]

#     print("per is ",sum/5)

# marks(a=88,b=99,c=77,d=76,e=45)

# lambda function - aisa fun jiska koi normal funs jasia name nahi hota ha 

# use one line functions define karna k liya
# syntax - lambda arguments : expression

# square = lambda x: x*x
# print(square(2))
# print(square(3))

# add = lambda a,b: a+b
# print(add(11,22))

# sub = lambda a,b: a-b
# print(sub(30,20))

# mult = lambda a,b : a*b
# print(mult(2,3))

# max = lambda a,b : a if a>b else b

# print(max(10,9))
# print(max(33,44))

# # map - map ka use kisi sequence ka data ka uper function apply karna k use hota ha 
# # to print list(map(square,l1)
# # syntax - map(function,iteriable)

# square = lambda x : x*x
# l1 = [2,4,5,6,8]

# print(list(map(square,l1)))

# filter - ka use sequence ka asia dataa ko joki s

# l1 = [2,4,5,6,8,7]
# l2 = list(filter(lambda x: x if x%2==0 else None ,l1))
# print(l2)

# sorted -  kisi sequence ka data ko sort karna ke liyee
# syntax - sorted(iterable,reverse,key)

# l1 = [22,44,11,55,77,88,56,86]

# l2 = sorted(l1)
# l3 = sorted(l1,reverse=True,key=None)
# ans = lambda x:x if x%2==0 else None
# l4 = sorted(l1,key=ans)
# # print(l3)
# # print(l2)
# # print(l1)
# print(l4)

# names = ["ajay","om","bhagya","raj","rajash"]
# print(names)
# names = sorted(names,key=len)
# print(names)

l1 = [34,28,44,61,52,10,73]
l2 = sorted(l1,key =lambda x:x%10)
print(l2)