# Creating a Class
# To create a class we need the key word class followed by the name and colon. Class name should be CamelCase.

# # syntax
# class ClassName:
#   code goes here

class person:
    pass
# print(person)

# output -- <class '__main__.person'>

# Creating an Object
# We can create an object by calling the class.

p = person()
print(p)

# output--<__main__.person object at 0x000001BA0FDD86E0>

# class methods
class Person:
    def __init__(self,name,):
        self.name = name

p1 = Person("john")
print(p1.name)
p1.age = 26
p1.city = "indore"

print(p1.age)
print(p1.city)