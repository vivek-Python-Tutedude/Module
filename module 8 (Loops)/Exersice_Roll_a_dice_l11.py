'''
write a program to simulate a roll of a dice 
A dice has 6 faces with no 1 - 6 written on them
The program should randomly print a no 1 - 6
'''
import random

print("welcome to the game of rolling dice")
while True :
    choice = input("Press 'r' to roll the dice or 'q to quit. : ")
    choice = choice.strip()
    if choice == 'q' :
        print("Thanks for playing the game, bye!")
        break
    elif choice == 'r' :
        print(f"Your Number is : {random.randint(1, 6)}")
    else :
        print("Invalid input!!")
print("GAME OVER!!")
        