# Class Constructor
# In the examples above, we have created an object from the Person class.
# However, a class without a constructor is not really useful in real applications.
#  Let us use constructor function to make our class more useful.
#  Like the constructor function in Java or JavaScript,
#  Python has also a built-in init() constructor function.
#  The init constructor function has self parameter which is a reference to the current instance of the class
#  Examples:

class Person:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name =name

p = Person('Sourabh Mehra')
print(p.name)
print(p)

# output >--
# Sourabh Mehra
# <__main__.Person object at 0x0000026DCF8586E0>

# Let us add more parameters to the constructor function.

class Person:
     def __init__(self,name,age,country,city,hobby):
          self.name = name
          self.age = age
          self.country = country
          self.city = city
          self.hobby = hobby
     def person_info(self):
          return (f"{self.name} is {self.age} years old and lives in {self.city} city of {self.country}.\nHis hobby is {self.hobby}")


p1 = Person('Sourabh Mehra',21,"India","Indore","learning")
print(f"name:{p1.name}")
print(p1.age)
print(p1.country)
print(p1.city)
print(p1.hobby)
print(p1.person_info())
p2 = Person('sahil Mehra',18,"India","Indore","chess playing")

print(f"name:{p2.name}")
print(p2.age)
print(p2.country)
print(p2.city)
print(p2.hobby)
print(p2.person_info())
# output <--
# name:Sourabh Mehra
# 21
# India
# Indore
# learning
# name:sahil Mehra
# 18
# India
# Indore
# chess playing