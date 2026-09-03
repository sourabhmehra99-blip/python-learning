# banking system by oops 
# contain class object encapsulation
class bank_system:
    def __init__(self,name,account_number,balance):
        self.name = name
        self.__acc = account_number
        self.balance = balance

    def display(self):
        print("Account Holder :",self.name)
        print("Account Number : XXXXX")
        print("Current balance :",self.balance)

    def deposit(self):
        print("---Deposit amount---")
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            self.balance += amount
            print("---Deposit succesfully---")
        elif amount <= 0:
            print("amount must be positive and not zero")
        else:
            print("Invalid statement.")

    def withdraw(self):
        print("---withdraw amount---")
        amount = int(input("Enter withdraw amount: "))

        if amount <= 0:
            print("amount must be positive.")
                   
        elif amount > self.balance:
           print("Insufficient balance.")
                    
        else:
           self.balance += amount
           print("---Withdraw succesfully---")

    def get_account_number(self):
        password = input("Enter the password: ")
        if password == "1234":
            print("Account Number:", self.__acc)
        else:
            print("wrong password\nTry again")
            

name = input("Enter the Account holder name: ")
account_number = int(input("Enter the Account number:"))
balance = float(input("Enter balance: "))

acc1 = bank_system(name,account_number,balance)

while True:
    print("---Bank system---")
    print("1. bank details")
    print("2. money deposit")
    print("3. money withdraw")
    print("4. See account number")
    print("5. Exit")

    choice = int(input("Enter your choice(1-5): "))
    if choice == 1:
        acc1.display()
    elif choice == 2:
        acc1.deposit()
        
    elif choice == 3:
        acc1.withdraw()
        
    elif choice == 4:
        acc1.get_account_number()
    elif choice == 5:
        print("Exit")
        break
    else:
        print("Invalid statement\nTry again")
