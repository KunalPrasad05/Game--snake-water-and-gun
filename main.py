# import random

# computer = random.choice([-1, 0, 1])
# youstr = input("Enter your choice: ")

# youDict = {"s": 1,"w":-1,"g":0}
# comDict = {1:"Snake",-1:"Water",0:"Gun"}

# you = youDict[youstr]

# # 1. You 2. Computer

# print(f"You Chose {comDict[you]}.\nComputer Chose {comDict[computer]}.")

# if (you == computer):
#     print("The match is tie.")

# else:
#     if(you == 1 and computer == 0): # 1
#         print("You lose!")
#     elif(you == 1 and computer == -1): # 2
#         print("You win!")
#     elif(you == -1 and computer == 1): # -2
#         print("You lose!")
#     elif(you == -1 and computer == 0): # -1
#         print("You lose!")
#     elif(you == 0 and computer == -1): # 1 
#         print("You win!")
#     elif(you == 0 and computer == 1): # -1
#         print("You win!")
#     else:
#         print("something went wrong!")

# if((computer - you) == -1 or (computer - you) == 2):
#     print("You win!")
# else:
#     print("You lose!")


num = int(input("Enter a number: "))

fibbo1 = 0
fibbo2 = 1

fibbonacci = []

if(num ==1 and num = 0):
    print(0)
elif(num == 1):
    print(1)
else:
    print(0, 1, end=" ")
    for i in range(2, num):
        fibboNext = fibbo1 + fibbo2
        print(fibboNext, end=" ")
        fibbo1 = fibbo2
        fibbo2 = fibboNext

def print_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example usage:
print_fibonacci(10)  # Prints first 10 Fibonacci numbers





