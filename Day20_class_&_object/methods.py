# The methods are functions which belong to the object.

class Car:
    def __init__(self,brand,model,colour):
        self.brand = brand
        self.model = model
        self.colour = colour

    def Car_info(self): # (self) provide the info by object
        return (f"car Brand : {self.brand}\ncar model : {self.model}\ncar colour :{self.colour}")

# car1 = Car("Audi","BE 5","black")
# print(car1.Car_info())

# Object Default Methods
# Sometimes, you may want to have default values for your object methods.
# If we give default values for the parameters in the constructor, 
# we can avoid errors when we call or instantiate our class without parameters.
#  Let's see how it looks:
#  Example:

class Person:
    def __init__(self,name ="username",age="default",city="indore"):
        self.name = name
        self.age = age
        self.city = city

    def person_info(self):
        return  (f"Name : {self.name}\nAge : {self.age}\nCity : {self.city}")

p1 = Person()
print(p1.person_info())
p2 = Person('john',21,'maxico')
print(p2.person_info())

# Output <--
# Name : username
# Age : default
# City : indore
# Name : john
# Age : 21
# City : maxico