# Challenge 1 — Number Analyzer

"""Write a program that takes 10 numbers from the user.

Your program should display:

1.How many numbers are positive
2.How many are negative
3.How many are zero
4.Sum of all numbers
5.Largest number
6.Smallest number
7.Average of the numbers """

#first take input of number of elements 
n = int(input("enter number of elements : "))

my_list = []
positive =0
negative = 0
zeros =0

for i in range(n):
    element = int(input("Enter the number : "))
    if element >0:
        positive +=1
    elif element <0:
        negative +=1
    else:
        zeros +=1

    my_list.append(element)



def output():
    print(f"the positive numbers : {positive}")
    print(f"the negative numbers : {negative}")
    print(f"the zeros numbers : {zeros}")
    print(f"the greatest number : {max(my_list)}")
    print(f"the smallest number : {min(my_list)}")
    print(f"the average of all number : {sum(my_list)/n}")
    print(f"the sum of the number: {sum(my_list)}")

output()