import random
again = "yes"
counting_tries = 1
while again == "yes":
    number = random.randint(1,100)
    guess = int(input("What is your guess? "))
    while guess != number:
        counting_tries = counting_tries + 1
        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
        guess = int(input("What is your guess? "))
    print("You guessed it!")
    print(f"It took you {counting_tries} guesses.")
    print()
    again = input("Would you play again (yes/no)? ")
    again = again.lower()
    print()
print("Thank you for playing. Goodbye.")