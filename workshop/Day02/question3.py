# rapido 0-1 20 rs - bass
# 1 -5 6 per km
# 6 - 12  5.5
# 12 - 20 5 
# 20 - we can deliver out city
# distance 

distance = float(input("Enter distance: "))

if (distance <= 1):
    print("the amount is 20 rupess.")
elif (distance >1 and distance <=5):
    print(f"the amount of fare is {distance * 6 + 20}")
elif (distance >6 and distance <=12):
    print(f"the amount of fare is {distance * 5.5 + 20}")
elif (distance >12 and distance <=20):
    print(f"the amount of fare is {distance * 5 + 20}")
else:
    print("we can give ride over 20 km.\nSorry for it")