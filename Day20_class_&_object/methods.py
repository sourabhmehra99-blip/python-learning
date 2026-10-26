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

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

# Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
# John Doe is 30 years old. He lives in Noman city, Nomanland.
# ['HTML', 'CSS', 'JavaScript']
# []