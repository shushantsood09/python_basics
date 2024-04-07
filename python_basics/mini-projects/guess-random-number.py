# Program to guess the random number as a game.

import random

target = random.randint(1, 100)
# print(target)

while True:
    userChoice = input("Guess the target or Quit(Q) : ")
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Correct Guess!")
        break
    elif(userChoice < target):
        print("Your number was small. Take a bigger guess")
    else:
        print("Your number was big. Take a smaller guess")

print("---------GAME OVER----------")