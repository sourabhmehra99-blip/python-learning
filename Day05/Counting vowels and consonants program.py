let = input("Enter the words: ")
vow = 0
con = 0
for x in range(len(str(let))):
   if let[x] in "AEIOUaeiou":
    vow +=1
   else:
     con+=1

print(f"{vow} number of vowel")
print(f"{con} number of consonants")

let = input("Enter the words: ")
vow = 0
con = 0
for x in let:
   if x in "AEIOUaeiou":
    vow +=1
   else:
     con+=1

print(f"{vow} number of vowel")
print(f"{con} number of consonants")
