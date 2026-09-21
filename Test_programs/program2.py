# ATM sumalator

def main_menu():
    
        print("----- ATM ----")
        print("1.check balance\n2.deposit amount\n3.withdraw amount\n4.Exit")

def Deposit(balance):
        try:
            amount = int(input("Enter the amount to deposit : "))
            if amount <=0:
                  raise ValueError("Amount should be greater than 0") 
            balance += amount
            print("Amount deposit succesfully")
            return balance
        except ValueError as error:
              print(error)
              return balance
        
def withdraw(balance):
      try:
            amount = int(input("Enter amount to withdraw : "))
            if amount <= 0 :
                  raise ValueError("Amount should be greater than 0")
            elif amount > balance:
                  raise ValueError("insufficient balance")
            else:
                  print("Amount withdraw succesfully")
                  balance -= amount
                  return balance
      except ValueError as error:
            print(error)
            return balance


balance = 10000

while True:
      main_menu()
      try:
         choice = int(input("Enter you choice : "))
         if choice == 1:
            print(f"the current balance in account : {balance}")
         elif choice == 2:
            balance = Deposit(balance)
         elif choice == 3:
            balance = withdraw(balance)
         elif choice == 4:
            print("Thanks you ")
            break
         else:
            print("Invalid statement")
      except ValueError:
           print("choice valid option")
            

                  
    