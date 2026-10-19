language = "python"
lst = list(language)
print(type(lst))
print(lst)

lst = [i for i in (language)]
print(lst)

number = [i for i in range(11) if i%2==0]
print(number)

square = [i*i for i in range(11)]
print(square)

# Filter numbers: let's filter out positive even numbers from the list below

numbers = [-8, -7, -3, -1, 0, 1, 2, 3, 4, 5, 7, 6, 8, 10]

positive_number = [i for i in numbers if i>0]
print(positive_number)

positive_even_number = [i for i in numbers if i%2==0 and i>0]
print(positive_even_number)