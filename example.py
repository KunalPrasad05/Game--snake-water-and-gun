import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")

youDict = {"s": 1,"w":-1,"g":0}
comDict = {1:"Snake",-1:"Water",0:"Gun"}

you = youDict[youstr]

# 1. You 2. Computer

print(f"You Chose {comDict[you]}.\nComputer Chose {comDict[computer]}.")

if (you == computer):
    print("The match is tie.")

if((computer - you) == -1 or (computer - you) == 2):
    print("You win!")
else:
    print("You lose!")