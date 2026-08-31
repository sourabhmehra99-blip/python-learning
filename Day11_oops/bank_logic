class bank_account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self):
        print("--- want to deposit amount ---")

        choice = input("Enter your choice Yes/No: ")
         
        if choice.lower() == "yes" :
            amount = float(input("Enter your amount: "))

            self.balance += amount
        elif choice.lower() == "no":
            print("thanks")
        else:
            print("Invalid statement")

    def display(self):
        print("Name",self.name)
        print("balance: ",self.balance)

name = input("Enter the name: ")
balance = float(input("Enter your balance: "))

acc1 = bank_account(name,balance)
acc1.deposit()
acc1.display()
