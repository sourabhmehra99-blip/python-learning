# simple intrest calculation
# give formula for simple intrest
# SI = (P * R * T) / 100
# where P = Principal, R = Rate of interest, T = Time

p = int(input("Enter the principal amount: "))
r = float(input("Enter the Rate of intrest: "))
time = int(input("Enter the time in year : "))

SI = (p * r * time)/ 100
total_amount = p + SI
print("the simple intrest is ",SI)
print("the total amount is ",total_amount)

