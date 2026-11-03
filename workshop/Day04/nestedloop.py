# print("===hello world===")

# for i in range(1,4):
#     for j in range(1,4):
#         print('i=',i,"j=",j)

#     print("==========")

# i = 1
# while i<4:
#     j = 1
#     while j<5:
#         print('i=',i,"j=",j)
#         j+=1
#     print("=========")
#     i+=1
    
#   prime number 
num = int(input("Enter number: "))

for i in range(1,num):
    isprime = True
    for j in range(2,i//2+1):
        if i % j == 0:
            isprime = False
            break
    if isprime:
        print(i)



