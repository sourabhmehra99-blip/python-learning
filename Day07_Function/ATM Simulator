
print("ATM Simulation")

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")



balance = 0
while True:

    choice = input("Enter your choice (1-4): ")

    match choice:
        case "1":
            if balance != 0:
                print(f"your balance is {balance}")
            else:
                print("Your balance is $0. Please deposit money.")
        case "2":
            deposit = float(input("Enter the amount to deposit: "))
            balance += deposit
            print(f"You have deposited ${deposit}. Your new balance is: ${balance}")
        case "3":
            withdraw = float(input("Enter the amount to withdraw: "))
            if withdraw <= balance: 
                balance -= withdraw
                print(f"You have withdrawn ${withdraw}. Your new balance is: ${balance}")
            else:
                print("Insufficient funds. Please check your balance.")
        case "4":
            print("Exiting the ATM simulation. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")
