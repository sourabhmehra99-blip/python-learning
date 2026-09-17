# ONLINE SHOPPING PRODUCT QUANTITY

stock = 10
try:
    quantity = int(input("Enter Quantity of product: "))
    if quantity <= 0:
        raise ValueError("quantity can't be negetive or zero")
    if quantity > stock:
        raise ValueError("not enough stock available")

    print("order placed succesfully")
except ValueError as error:
    print("purchase failed ", error)