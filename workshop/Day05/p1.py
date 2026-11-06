num = [22,44,33,11,99,77]

for i in range(len(num)):
    for j in range(len(num)-i-1):
        if num[j] > num[j+1]:
            temp = num[j+1]
            num[j+1] = num[j]
            num[j] = temp


print(num)



