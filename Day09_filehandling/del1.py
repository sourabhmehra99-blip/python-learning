# Deleting file

# We have seen in previous section, how to make and remove a directory using os module.
#  Again now, if we want to remove a file we use os module.

# import os
# os.remove('./files/example.txt')

import os

if os.path.exists("Day09_filehandling/quest"):
    os.remove("Day09_filehandling/quest")
else:
    print("the file does not exist")