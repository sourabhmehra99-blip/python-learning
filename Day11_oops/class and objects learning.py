class Car:
    def __init__(self,brand,colour,milege):
        self.brand = brand
        self.colour = colour
        self.milege = milege

    def car_details(self):
        print(f"Car brand is {self.brand}.Colour is {self.colour}\nMilege of car {self.milege}")

car1 = Car("Tata","black",25)
car2 = Car("Bmw","purple",15)

car1.car_details()

car2.car_details()
