# list 

thislist = ["apple","banana","grapes","cherry"]

print(type(thislist))

# output --<class 'list'>

# access list by loop
for i in thislist:
    print(i)

#  Access elements by index
print(thislist[0]) # apple
print(thislist[1]) # banana
print(thislist[2]) # grapes
print(thislist[3]) # cherry

# Add new items

thislist.append("papaya")
for i in thislist:
    print(i)

# apple
# banana
# grapes
# cherry
# papaya

# remove a item

thislist.remove("apple")
for fruit in thislist:
    print(fruit)

# banana
# grapes
# cherry