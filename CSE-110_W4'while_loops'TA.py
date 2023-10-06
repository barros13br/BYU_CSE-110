#hello
import random

play = "yes"

while play.lower() == "yes":    
    number = random.randint(1, 100)

    guess = -1

    while guess != number:
        guess = int(input("Guess the magic number "))

        if guess > number:
            print("Lower")
        elif guess < number:
            print ("Higher")
        else:
            print ("You Guessed it!")
    play = input ("Want to play again? ")

print("THE END")