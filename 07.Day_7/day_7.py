"""
This project is HangMan
"""
# ============================== Imports ========================================================#
import random
from hangman_art import hangman_stages, hangman_word_list


# =================================== Variables =================================================#

word = random.choice(hangman_word_list).lower()
lista = ["_" for _ in range(len(word))]
lives = len(hangman_stages) - 1

# ==================================== Board ====================================================#
print(lista)
print(hangman_stages[lives])

# ================================================================================================#
# ======================= Game Logic =============================================================#

while "_" in lista and lives > 0:
    guess = input("Please choose a letter you believe to be in the word: ").lower()
    if guess in word:
        for position, letter in enumerate(word):
            if letter == guess:
                lista[position] = letter
    else:
        lives -= 1
        print(hangman_stages[len(hangman_stages) - lives - 1])
        print(f"Wrong Guess! you have {lives} left.")
    print(lista)
if "_" not in lista:
    print("Congratz you won!")
else:
    print("You are all out of lives. The word was: ", word)
