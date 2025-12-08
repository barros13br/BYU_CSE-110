# word = "mosiah" nosiha
# print("Your hint is: ",end="")
# for letter_index in range(len(word)):
#     letter = word[letter_index]
#     print ("_", end="")

# guess = input("What is your guess? ")
# while guess != word:
#     for guess_index in range(len(guess)):
#         guess_letter = guess[guess_index]
#         if

# colocar uma palabra chave OK
# dar dica OK
# comparar a tentativa com a palavra chave 
# se a letra atual da tentativa tiver na palavra chave e no mesmo index, letra maiuscula.
# se a letra atual da tentativa tiver na palavra chave mas não no mesmo index, letra minuscula.
# se a letra atual da tentativa não existir, colocar _.

# a tentativa deve ter o mesmo numero de letras (contar a quantidade de length da palavra chave).
# contar as tentativas

print("Welcome to the word guessing game!")
print()
key_word = "mosiah"
number_of_tries = 1
print("Your hint is: ", end="")
for letter_index in range(len(key_word)):
    letter = key_word[letter_index]
    print("_ ", end="")
print()
guess = input(f"It has {len(key_word)} letters. What is your guess? ")

while len(guess) != len(key_word):
    print("Sorry, the guess must have the same number of letters as the secret word.")
    print()
    guess = input(f"What is your guess? [Remember, it should have {len(key_word)} letters]: ")

for index in range(len(key_word)):
    guess_letter = guess[index]
    key_letter = key_word[index]
    if guess_letter == key_letter and guess_letter[index] == key_letter[index]:
        print(key_letter.upper(), end="")
    elif guess_letter == key_letter and guess_letter[index] != key_letter[index]:
        print(guess_letter.lower(), end="")
    else:
        print("_", end="")