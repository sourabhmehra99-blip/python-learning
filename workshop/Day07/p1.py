# LIST COMPRESSION

list = [3,4,5-3,-4,77,55,-88,9]

list2 = [i for i in list]
list3 = [i for i in list if i>0]

print(list)
print(list2)
print(list3)

list = [i for i in range(21) if i%2==0]
print(list)     #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


l5 = [list[i] for i in range((len(list)//2)+1)]
print(l5)

l1 = [1,2,3,4,5,6,7]

l2 = [i*i for i in l1]
l3 = [i*i*i for i in l1]

print(l1)
print(l2)
print(l3)

L4 = [2,3,4,5,6,7,8]

L5 =["even" if i%2==0 else "odd" for i in L4]
print(L5)

l1 = [2,3,4,5,64,7,78,8,5,34,55,15,44,30,33]

l6 =[i for i in l1 if i%5==0]
l7 = [i for i in l1 if (i%5==0) and (i%3==0)]
l8 =[i for i in l1 if(i %10 ==4)]
print(l6)
print(l7)
print(l8)

name = "RAHUL"
L6 = [i for i in name]
print(L6)

names = ["JAY","rahul","OM","ram"]
l4 = [i.upper() for i in names]
l5 = [i.title() for i in names]
l6 = [i for i in names if(i.isupper())] 
l7 = [ len(i) for i in names ]
print(names)
print(l4) 
print(l5)
print(l6)
print(l7)

s = "hello E python is a programming language"

vowels = [i for i in s if (i.lower() in "aeiou")]
print(vowels)

# nested list comprehension
list = [[i for i in range(1,4)] for j in range(1,4)]
print(list)

list = [[(i) for i in range(1,4)]for j in range(1,4)]
print(list)