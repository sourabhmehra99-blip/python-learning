# vowel finding program
vowel = input("Enter the character: ")
vowel = vowel.upper()
if len(vowel) == 1:
    if vowel.isalpha():
       
     if vowel in "AEIOU":
        print("---Vowel---")
     else:
       print("---consonant---")
    else:
       print("Enter an vaild alphabat.")
else :
   print("many characters")
