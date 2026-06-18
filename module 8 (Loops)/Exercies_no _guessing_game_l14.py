# Number guessing game
import random
num = random.randint(1, 50)
print("Wwlcome to the guess the Number Game!!")
print("The secret number is between 1 and 50")
counter = 10
while True :
    if counter == 0 :
        print(f"{counter} attrmpts left")
        break
    print(f"You have {counter} attempts left.")
    choice = int(input("Enter your guess : "))
    if choice == num :
        print("Congrates your guess is correct!")
        break
    elif choice > num :
        print("Your guess is wrong! Try Lower")
        counter = counter - 1
    elif choice < num :
        print("Your guess is wrong! Try Higher")
        counter = counter - 1
    else :
        print("Invalid Choice!")
if counter == 0 :
    print("Bad luck!! You exhausted all your attempts and couldn't guess the number.")
    print(f"The secret no  was {num}. Game Over!!")