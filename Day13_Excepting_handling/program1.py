# ATM withdrawal 

balance = 10000

try:
    amount = int(input("Enter amount to withdrawal : "))

    if amount <= 0:
        raise ValueError("amount could not be zero or less ")
    elif amount > balance:
        raise ValueError("insufficient balance")
    else:
        balance -= amount
        print("amount withdrawal sucessfully ")
except ValueError as error :
    print("Transaction failed :",error)