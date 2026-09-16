# student login system
#step 1: enter username , password 
user = input("Enter username: ").upper()
password = input("Enter password: ")

if (user == "SOURABH MEHRA"):

     if(password == "2304"):
        print("---login succesfully!---")
     else:
        print("---Wrong password---")
else:
    print("---Wrong username---")

added more 
# student login system
#step 1: enter username , password 
user = input("Enter username: ")
password = input("Enter password: ")

if (user =="Sourabh Mehra" and password == "2304"):
    print("---login succesfully---")
elif (user =="Sourabh Mehra" and password != "2304"):
      print("---Wrong password---")
elif (user !="Sourabh Mehra" and password == "2304"):
      print("---Wrong Username---")
else:
     print("wrong username and password")
