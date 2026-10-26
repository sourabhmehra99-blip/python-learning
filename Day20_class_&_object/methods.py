# The methods are functions which belong to the object.

class Car:
    def __init__(self,brand,model,colour):
        self.brand = brand
        self.model = model
        self.colour = colour

    def Car_info(self): # (self) provide the info by object
        return (f"car Brand : {self.brand}\ncar model : {self.model}\ncar colour :{self.colour}")

car1 = Car("Audi","BE 5","black")
print(car1.Car_info())