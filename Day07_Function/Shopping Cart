# Shopping Cart

cart = []

print("Shopping Cart Simulation")

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. total Price")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter the item name to add: ")
        price = float(input("Enter the price of the item: "))
        cart.append((item, price))
        print(f"{item} has been added to the cart.")
    elif choice == "2":
        item = input("Enter the item name to remove: ")
        for product in cart:
            if product[0] == item:
                cart.remove(product)
                print(f"{item} has been removed from the cart.")
                break
        else:
            print(f"{item} is not in the cart.")
    elif choice == "3":
        if cart:
            print("Items in your cart:")
            for item, price in cart:
                print(f"{item}: ${price}")
        else:
            print("Your cart is empty.")
    elif choice == "4":
        total_price = sum(price for _, price in cart)
        print(f"The total price of items in your cart is: ${total_price}")
    elif choice == "5":
        print("Exiting the Shopping Cart simulation. Goodbye!")
        break
    else:
        print("invalid choice. Please try again.")
