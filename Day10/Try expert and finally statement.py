age = input("Enter your age: ")

try:
    age = int(age)
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        print("You are a minor.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
except ValueError as e:
    print(f"Invalid input: {e}")
finally:
    print("Thank you for using the age classification program.")
