# list -- ordered,indexed,mutable,duplec allowed
# tuple -- ordered ,indexed,inmutable,duplecate allowed
# set -- unorderd,unindexed,mutable,not allow duplecate

s1 = set()
print(type(s1))


set = {1,2,3,4}
print(type(set)) 

s3 = {12,"raj",66.99,True}
# print(s3) # it give random order

s3.add("rahul") # add rahul 
# print(s3)

s3.update([11,22,33,44]) # it use for update multiple value 
print(s3) 
# {'rahul', True, 66.99, 33, 'raj', 11, 12, 44, 22}
s3.remove(2)  # remove if element exist and if not in set give error
print(s3)
s3.discard(22) # dont give error
print(s3)

print(s3.pop()) # give random values

s3.clear()
print(s3)

s1 = {11,22,33,44,55}
s2 = {66,44,55,77,88,99}

print(s1.union(s2))                # all set add
print(s1.intersection(s2))         # comman elements
print(s1.difference(s2))           # different element of s1 set
print(s1.symmetric_difference(s2)) # gives all different element of both sets

a = {1,2,3,4,5}
b = {1,2,3}

print(a.issuperset(b))      # True
print(a.issubset(b))        # False
print(b.issubset(a))        # True

c = {11,22,33}
d = {44,55,66}

print(c.isdisjoint(d))      # Ture,All elements are different in both sets

emp = {"agmail.com","bgmail.com","cgmail.com"}
sm = {"cgmail.com","egmail.com","dgmail.com"}

# emp = emp.difference(sm)

emp.difference_update(sm) 
print(emp)
print(sm)
print(emp.isdisjoint(sm))
