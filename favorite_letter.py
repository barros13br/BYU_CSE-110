word = "commitment"
favorite_letter = input("What is your favorite letter? ")
print()

for letter_index in range(len(word)):
    letter = word[letter_index]
    if favorite_letter == letter:
        print("_", end="")
    else:
        print(letter, end="")