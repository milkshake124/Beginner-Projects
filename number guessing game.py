print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100. \nYou have 5 chances to guess the correct number")
import random
chance = 0
attempts = 0
randNum = random.randint(1, 100)
print("Please select the difficulty level: \n1. Easy (10 chances) \n2. Medium (5 chances) \n3. Hard (3 chances)")
difficulty = int(input("Please enter your difficulty level: "))
if difficulty == 1:
    chance = chance + 10
    print("Great! You have selected the Easy difficulty level.\nLet's start the game!")
elif difficulty == 2:
    chance = chance + 5
    print("Great! You have selected the Medium difficulty level.\nLet's start the game!")
elif difficulty == 3:
    chance = chance + 3
    print("Great! You have selected the Difficult difficulty level.\nLet's start the game!")

for x in range(chance):
    guess = int(input("Enter your guess: "))  # ✅
    if guess < randNum:
        attempts = attempts + 1
        print("Incorrect! The number is more than", guess)
    elif guess > randNum:
        attempts = attempts + 1
        print("Incorrect! The number is less than", guess)
    elif guess == randNum:
        attempts = attempts + 1
        print("Congratulations! You guessed the correct number in", attempts, "attempts")  # ✅


        

