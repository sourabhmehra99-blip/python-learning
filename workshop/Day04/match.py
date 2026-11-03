number = int(input("Enter any number 1 to 10 : "))

match number:
    case 1:
        print("one")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case 6:
        print("six")
    case 7:
        print("Seven")
    case 8:
        print("Eight")
    case 9:
            print("nine")
    case 10:
            print("Ten")
    case _:
        print("not valid")

balance = 3000
while True:
    print("1. Check balance\n2. deposit\n3. withdrawl\n4. Exit")
    
    choice = int(input("Enter your choice(1-4): "))

    match choice:
        case 1:
            print(f"your balance : {balance}")
        case 2:
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print(f"your balance : {balance}")
        case 3:
            amount = int(input("Enter withdrawl amount: "))
            if amount > balance:
                print("Insuffecient amount")
            else:
                balance -= amount
                print(f"your balance : {balance}")
        case 4:
            print("Exiting")
            break
        case _:
            print("Invalid choice...")
            

num = int(input("Enter your number : "))
i =2
isprime = True

# while i<=num//2+1:
#     isprime = False
#     i+=1
#     break

for j in range(2,num//2+1):
    if num % j == 0:
        isprime = False
        break

if isprime:
    print(" prime")
else:
    print("not a prime")

num = int(input("Enter the number: "))
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count +=1

if count >2:
    print("Not a prime number.")
else:
    print("A prime number.")
