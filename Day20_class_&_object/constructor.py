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