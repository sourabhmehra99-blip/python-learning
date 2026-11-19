# dictionary 
# dtct = { "key":value } unique key but values can be ducplcate

dict = {"roll":12,"name":"jay"}

print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())

for i in dict.keys():
    print(i)

for i in dict.values():
    print(i)

for i in dict.items():
    print(i)

for x,y in dict.items():        
    print("[",x,":",y,"]")      

# [ roll : 12 ]
# [ name : jay ]

cont = {"akash":1234,"ram":3456,"raj":46765}

print(cont["akash"])    # gives values of akash when it have not key it gives error
print(cont.get("ram"))  # gives values of ram it does not give error if key not exixt

cont.update({"priya":1234})
print(cont) 

cont.update({"akash": 2233}) # if key exists it update value
print(cont)

cont.setdefault("priya",2344) # update data
cont.setdefault("akash",4455) # if key exists it does not update value
print(cont)

cont["ram"] = 1234    # it also use for add
print(cont) 

del cont["akash"] # delete 
print(cont)

cont.pop("ram")
print(cont)

cont.popitem()  # delete last item of dectionary
print(cont)

new_cont = cont.copy() 
print(new_cont)

new_cont.clear()
print(new_cont)

cont = {"akash":1234,"ram":3456,"raj":46765}

cont.fromkeys(["jayveer","ajaa","Ramesh"])
print(cont)

# #--------------------------Nested Dictionary -----------------------------

a1 = {1:{"akash":1234,},2:{"raj":46765}}
print(a1[1]["akash"])