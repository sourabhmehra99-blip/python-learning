# ATM withdrawal program

balance = 20000
try:
    amount = int(input("Enter amount to withdrawal: "))
    if amount > balance:
        raise ValueError("insufficent balance") 

    balance = balance - amount
    print("withdrawal succesfully")
    print("Remaining balance : ",balance)
except ValueError as error:
    print("Transation failed: ",error)