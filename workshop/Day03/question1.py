# balance menu program

balance = 3000

while True:
    print("1. Check balance\n2. deposit\n3. withdrawl\n4. Exit")

    choice = int(input("Enter your choice(1-4): "))

    if choice == 1:
        print(f"Balance : {balance}")
    elif choice == 2:
        amount = int(input("Enter you deposit amount : "))
        balance += amount
        print(f"your balance : {balance}")
    elif choice == 3:
        amount = int(input("Enter amount to withdrawl : "))
        if amount > balance:
            print("Insufficient balance ")
        else:
            balance -= amount 
            print(f"your balance : {balance}")
    elif choice == 4:
        print("Exiting menu")
        break
    else:
        print("Invalid choice !\nTry again")