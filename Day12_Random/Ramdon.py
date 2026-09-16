import random as rd
words =["fire","earth","water","Air","space"]
word = rd.choice(words)
guess_word = ["_"] *len(word)
attempts = 6

print("===Hangman Game ===")
while(attempts >0):
    print(f"Attempts left : {attempts}")
    print("Word"," ".join(guess_word))

    guess = input("Enter your guess letter : ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guess_word[i] = guess
                print("=== Correct letter ===")
    else:
        print("Wrong letter!!!")
        attempts -= 1
        

    if "_" not in guess_word:
        print("You win the game!!!")
        print(f"the word is {word}")
        break
else:
    print("you loss the game!!!")
    print(f"the word is {word}")
