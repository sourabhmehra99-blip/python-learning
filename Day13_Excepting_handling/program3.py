# Division bussiness report

# using ZeroDivisionError

try:
    total_sales = 50000
    number_of_days = int(input("Enter the number of days : "))

    average = total_sales / number_of_days
    print("Average daily sales : ",average)
except ZeroDivisionError:
    print("Number of days cannot be zero")

except ValueError:
    print('Please enter valid number')