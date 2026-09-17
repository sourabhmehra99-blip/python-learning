# Rock,paper,Scissor Game

import random as rd

comp = ["paper","rock","scissor"]

attempts = int(input("Enter match (3-5-7): "))
win =0
loss=0
tie =0
round = 0
while attempts >0:
    print(f"Match number {round +1}")
    print("Rock\npaper\nScissor\n")
    computer = rd.choice(comp)
    choice = input("Enter you choice : ").lower()
    if choice in comp:
      print(f"computer choice : {computer}")
      if computer == choice:
          print("the match tie!!") 
          tie +=1
          
      elif computer == "rock":
        if choice == "paper":
            print("you win this match!!")
            win +=1
        else:
            print("you loss the match!!!")
            loss +=1
            
      elif computer == "paper":
        if choice == "scissor":
            print("you win this match!!!")
            win +=1
        else:
             print("you loss the match!!!")
             loss +=1
             
      elif computer == "scissor":
        if choice == "rock":
            print("you win this match!!")
            win +=1
        else:
            print("you loss the match!!!")
            loss +=1 
            
      attempts -=1 
      round +=1     
    else:
        print("Invalid choice\ntry again!!!")
    

else:
    print("you final score")
    print(f"wins : {win}")
    print(f"loss : {loss}")
    print(f"Tie : {tie}")

