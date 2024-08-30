import random

hidden_Num=random.randint(1,10)

while True:
    userGuess=int(input("Guess a number: "))
    if userGuess>hidden_Num:
        print("Too High!")

    if userGuess<hidden_Num:
        print("Too Low!")

    if userGuess==hidden_Num:
        print("You are correct!")
        break