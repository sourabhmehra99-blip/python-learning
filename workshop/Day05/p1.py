# # string 

# a="Hello, World!"
# b = 'hello'
# c = '''This is a multi-line string.'''

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

# a = "python"
# b = "Python"

# print(a==b) 
# print(a is b)

# # indexing
# print(a[0]) # p
# print(a[1]) # y

# # negative indexing
# print(a[-1]) # n    
# print(a[-2]) # o

# slicing -string[start:stop:step]
# a = "python programming language"

# print(a)
# print(a[0:6])  # python
# print(a[:6])
# print(a[0:6:1])
# print(a[::]) # python programming language
# print(a[::2]) # pto rgamn agae

# # negatice slicing
 
# print(a[-1:-9:-1]) # egaugnal
# print(a[-9:-1:1])  # languag
# print(a[::-1]) # egaugnal gnimmargorp nohtyp

# a = "rahul"
# print(a.upper())

# new = a.upper()
# print(new)
# print(new.lower())

s = "python programming language"

# print(s.capitalize()) # Python programming language
# print(s.title())      # Python Programming Language
# print(s.islower())    # True

# w = "PyThOn proGRamMing lanGuaGe"

# print(w.swapcase()) # pYtHoN PROgraMMING LANgUAgE
# print(w.casefold()) # python programming language
# print(w.islower()) # False
# print(w.isupper()) # False
# print(s is w) # False
# print(s.casefold() == w.casefold()) # True

# s = " Yellow fox jumps over the lazy fox "

# print(s.find("fox"))  # 8
# print(s.find("fog"))  # -1
# print(s.rfind("fox")) # 32

# print(s.index("o"))   # 8
# print(s.rindex("o"))  # 33

# print(s.count("Yellow")) # 1
# print(s.count("fox"))    # 2

# username = "priyanshu123"
# print(username.isalnum())  # True
# print(username.isalpha())  # False

# password = "priyanshu@123"
# print(password.isalnum())  # False
# print(password.isalpha())  # False
# print(password.isdigit()) # False
# print(password.isspace()) # False

# a = "  "
# print(a.isspace()) # True

# c = "\t"
# print(c.isspace()) # True

# d = "\n"
# print(d.isspace()) # True

# b = "  rahul"
# print(b.isspace()) # False

# _ = "1234.55"
# __ = "1234"
# print(_.isdecimal()) # False
# print(__.isdigit())   # True

# a = "   python progrmming language        "
# print(a) #   python progrmming language
# print("'",a.strip(),"'") # python progrmming language
# print(a.lstrip()) # python progrmming language
# print(a.rstrip()) #    python progrmming language

# s = "today! priyanshu wants to eat panipuri  kya aaj priyanshu ko panipuri kha payaga"
# lst = s.split()

# for i in lst:
#     print(i)

# # concatenation
# a = "priyanshu"
# b = "yadav"
# print(a.capitalize() +" "+b.capitalize()) # Priyanshu Yadav

# # WAP to reverse a string
# s = "python"

# rev = s[::-1]
# print(rev) # nohtyp

# name = input("Enter your name: ")
# rev ="" 

# for i in reversed(name):
#     rev += i

# print(f"Reverse is {rev}")
# print(f"Original is {name}")

# if( name == rev):
#     print("Palindrome string")
# else:
#     print("Not Palindrome string")

# WAP to number in words

# sentance = input("Enter a sentence: ")
# words = sentance.split()

# print("Number of words in the sentence:", len(words))
# print("Words in the sentence:",len(sentance.split()))

password = input("Enter your password: ")
cap = False
dig = False
sma = False
spe = False
if len(password) >= 8:
    for ch in password:
        if ch.isupper():
            cap = True
        elif ch.islower():
            sma = True
        elif ch.isdigit():
            dig = True
        else:
            spe = True
else:
    print("Password must be at least 8 characters long")

if cap and sma and dig and spe:
    print("Strong password")
else:
    print("Weak password")


   
    