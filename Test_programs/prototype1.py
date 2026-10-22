# prototype 1 
# unit conversion website

def distance():
    while True:
     print("---------- length conversion ----------")
     print("1.convert km to meter")
     print("2.convert km to cm")
     print("3.convert km to mm")
     print("4.convert mm to km")
     print("5.convert cm to km")
     print("6.convert meter to km")
     print("7.Exit")
    
     try:
        choice = int(input("Enter your choice(1-7):"))
        if choice == 1:
                km = float(input("Enter the distance in km: "))
                meter = km *1000
                print(f"the km: {km:.2f} in meter: {meter:.2f}")
        elif choice ==2:
                km = float(input("Enter the distance in km: "))
                cm = km *100000
                print(f"the km: {km:.2f} in centimeter: {cm:.2f}")
        elif choice == 3:
                km = float(input("Enter the distance in km: "))
                mm = km * 1000000
                print(f"the km: {km:.2f} in millimeter: {mm:.2f}")
        elif choice == 4:
                mm = float(input("Enter the length in mm: "))
                km = mm/1000000
                print(f"the mm:{mm:.2f} in km: {km:.2f} ")
        elif choice ==5:
                cm = float(input("Enter the length in cm: "))
                km = cm/100000
                print(f"the cm :{cm:.2f} in km: {km:.2f}")
        elif choice == 6:
                meter = float(input("Enter length in meter :"))
                km = meter/1000
                print(f"the meter: {meter:.2f} in km: {km:.2f}")
        elif choice == 7:
                print("Thanks for using unit converstion!")
                break
        else:
                print("Invalid choice ! Try again")

     except ValueError:
        print("Invalid input! Please enter a valid number.")


def temprature():
    while True:
        print("---------- temprature conversion ----------")
        print("1.convert celsius to all")
        print("2.convert fahrenheit to all")
        print("3.convert kelvin to all")
        print("4.Exit")

    
        choice =int(input("Enter your choice(1-4): "))
        try:
            if choice == 1:
                cel = float(input("Enter temprature in celsius: "))
                fah = (cel *9/5) + 32
                kel = cel + 273.25
                print(f"The temprature in celsius: {cel:.2f}\nThe temprature in fahrenheit: {fah:.2f}\nThe temprature in kelvin: {kel:.2f}")
            elif choice == 2:
                fah = float(input("Enter temprature in fahrenheit: "))
                cel = (fah -32)*5/9
                kel = (fah -32)*5/9 + 273.15
                print(f"The temprature in celsius: {cel:.2f}\nThe temprature in fahrenheit: {fah:.2f}\nThe temprature in kelvin: {kel:.2f}")
            elif choice == 3:
                kel = float(input("Enter temprature in kelvin: "))
                cel = kel -273.15
                fah = (kel-273.15)*9/5 +32
                print(f"The temprature in celsius: {cel:.2f}\nThe temprature in fahrenheit: {fah:.2f}\nThe temprature in kelvin: {kel:.2f}")
            elif choice == 4:
                  print("Thanks for using conversion")
                  break
            else:
                  print("Invalid choice!\nChoose between (1-4)")
        except ValueError:
              print("Invalid statement ")

def main_menu():
    while True:
      print("---------- unit conversion ----------")
      print("1.conversion lenghts")
      print("2.conversion temprature")
      print("3.Exit")
    
      choice = int(input("Enter your choice(1-2): "))
      if choice ==1:
          distance()
      elif choice == 2:
          temprature()
      elif choice == 3:
        print("Exit the program")
        break
      else:
          print("Invalid choice!")

main_menu()
      


      
            
