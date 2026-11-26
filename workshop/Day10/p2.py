# import datetime as dt

# #Current date and time 
# now = dt.datetime.now()
# print(now)

# # current date

# today = dt.date.today()
# print(today)

# #current time
# time = dt.datetime.now().time()
# print(time)

# #create custom date
# d = dt.date(2026,11,22)
# print(d)

# # Extract date components
# print("Year: ",today.year)
# print("Month: ",today.month)
# print("Day:",today.day)

# # Format date
# print(now.strftime("%d-%m-%Y"))
# print(now.strftime("%H:%M:%S"))


# # date1 = dt.date(2026,11,22)
# # date2 = dt.date(2026,12,1)
# # print("DIfference" ,date2 - date2)

# import os

# # Current working directory
# # print(os.getcwd())

# # list files and folders
# print(os.listdir())

# # create folder
# # os.mkdir("MYfolder")

# # check directory
# print(os.path.isdir("MYfolder"))

# # check file
# print(os.path.isfile("text.txt"))

# # join paths
# path = os.path.join("myfolder","text.txt")
# print(path)

# # rename folder
# # os.rename("myfolder","newfolder")

# # Rename empty folder
# os.rmdir("newfolder")

# import sys

# #1. python version

# print("python Version: ",sys.version)
# print("version Info:",sys.version_info)

# #2. platform info
# print("platform: ",sys.platform)
# # 3. command line arguments
# print("Argument Count",len(sys.argv))

# # 4. Number of Arguments 
# print("Argument Count : ",len(sys.argv))

# # 5. python Module search path
# print("python path",sys.path)

# # 6. Maximum Integer size
# print("Max integer size", sys.maxsize)

# # 7.Recursion limit

# print("recurdion :",sys.getrecursionlimit())

# # 8. change recursion limit

# sys.setrecursionlimit(2000)
# print("New limit " ,sys.getrecursionlimit())

# # 9. size of object in bytes

# a= 100
# print("object size; ",sys.getsizeof(a))

# # 10. standard output

# sys.stdout.write("hello python\n")

# # 11. standard input
# name = sys.stdin.readline()
# print("name: ",name)

# # Exit program
# # sys.exit()

# # 14. get python Executable location

# print("python Executable: ",sys.executable)
# print("code ends here")

import sys

print("Argument : ",sys.argv)
print("Aggument : ",len(sys.argv))

print("Program naem : ",sys.argv[0])

if len(sys.argv) > 1:
    for i in sys.argv:
        print(i)