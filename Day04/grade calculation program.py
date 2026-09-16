# grade calculation program:

print("""1.ENGLISH
2.HINDI
3.MATHS
4.SCIENCE
5.SOCIAL SCIENCE
""")

sub = list(map(int, input("Enter the subject marks: ").split()))


print(sub)

sum = sub[0] + sub[1] + sub[2] +sub[3]+sub[4]
per = (sum / 500) *100

if (per >=90):
    print(f"{per }%\nGrade is A++")
elif(per >=80):
    print(f"{per }%\nGrade is A+")
elif(per >=70):
    print(f"{per }%\nGrade is B+")
elif(per>= 50):
    print(f"{per }%\nGrade is C+")
elif(per >= 30):
    print(f"{per }%\nGrade is D")
else:
    print(f"{per} fail.")
