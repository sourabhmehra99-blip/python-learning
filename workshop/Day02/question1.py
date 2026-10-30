# question

# greater b/w 4 number
# simple intrest calculation
# rapido 0-1 20 rs - bass
# 1 -5 6 per km
# 6 - 12  5.5
# 12 - 20 5 
# 20 - we can deliver out city
# distance 

# Greater between 4 number

a,b,c,d = map(int, input("Enter four number: ").split())
if (a==b==c==d):
    print("all 4 number is equal")
else:
   if (a>b) and (a>c) and (a>d):
       print(a, "is greater" )
   else:
       if (b>c) and (b>d):
           print(b,"is greater")
       else:
           if(c>d):
               print(c,"is greater")
           else:
               print(d , "is greater")



# using max and min function 
# not usong map function

n = [int(x) for x in input("Enter 4 number: ").split()]
if (len(n)==4):
    if (n[0]==n[1]==n[2]==n[3]):
        print("All 4 number is equal.")
    else:
        print("Greatest number: ",max(n))
        print("Smallest number: ",min(n))
else:
    print("need only 4 numbers.")