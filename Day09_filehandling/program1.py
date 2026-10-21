# File Handling

# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# f = open("quest","r") 
# lines = f.read()
# print(lines)
# f.close()
# # output
# # hello world 
# # my name is sourabh mehra!hello world 
# # my name is sourabh mehra!

# print("===========")

# f = open("quest","r") 
# lines = f.readlines()
# print(lines)
# f.close()
# #output 
# #['hello world \n', 'my name is sourabh mehra!hello world \n', 'my name is sourabh mehra!']

# print("=============")

# f = open("quest","r") 
# lines = f.read().splitlines()
# print(lines)
# f.close()

# # output 
# # ['hello world ', 'my name is sourabh mehra!hello world ', 'my name is sourabh mehra!']


# with open("quest","w") as file:
#     lines = file.write('hello world')
#     print(lines)

# output it write the string in text file and output will given it 11 


with open("quest","r+") as file:
    lines = file.read().splitlines()
    print(type(lines))
    print(lines)

# output 
# <class 'list'>
# ['hello world']

    
    