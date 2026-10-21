
f = open("quest","r") 
lines = f.read()
print(lines)
f.close()
# # output
# # hello world 
# # my name is sourabh mehra!hello world 
# # my name is sourabh mehra!



f = open("quest","r") 
lines = f.readlines()
print(lines)
f.close()
# #output 
# #['hello world \n', 'my name is sourabh mehra!hello world \n', 'my name is sourabh mehra!']



f = open("quest","r") 
lines = f.read().splitlines()
print(lines)
f.close()

# # output 
# # ['hello world ', 'my name is sourabh mehra!hello world ', 'my name is sourabh mehra!']


with open("quest","w") as file:
    lines = file.write('hello world')
    print(lines)

# output it write the string in text file and output will given it 11 


with open("quest","r+") as file:
    lines = file.read().splitlines()
    print(type(lines))
    print(lines)

# output 
# <class 'list'>
# ['hello world']

    
    