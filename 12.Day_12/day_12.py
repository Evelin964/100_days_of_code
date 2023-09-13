"""THis is my day 12 project - A number guessing game.
    """

##======================== IMPORTS ================================##
import random
import webbrowser
from day_12_art import LOGO, PRINT_BREAKER


##=================================================================##
##                              DEF ZONE                           ##
LINK = "https://www.instagram.com/reel/CtjOYCULM8Z/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="


def hot_cold(number_to_guess=int, guess=int) -> int:
    """Tells you if you are close or not!

    Args:
        number_to_guess int: the number you need to guess
        guess int: the guess of the player
    """
    if guess < number_to_guess:
        print("You need to go higher!")
    elif guess > number_to_guess:
        print("You neeed to go lower")
    elif number_to_guess == guess:
        print(f"Correct! The number is {number_to_guess}")

        return number_to_guess


def difficulty(val: str) -> int:
    """Lets you choose a dificulty

    Args:
        val (str): take the type of game you want to play (easy or hard)

    Returns:
        int: the number of lives based on your game choice
    """
    assert val in ["hard", "easy"], "Invalid value, Please provide 'hard' or 'easy'. "
    if val == "hard":
        print("You have 5 chances to win the game! Goodluck!")
        return 5
    elif val == "easy":
        print("You have 10 chances to win the game. Fkin chicken!")
        return 10


def nr_guess_value() -> int:
    """This function returns a random value for you to guess

    Returns:
        int: returns an integer to guess
    """
    valoare = range(0, 101)
    return random.choice(valoare)


##==================================================================##
##                              MAIN ZONE                           ##


def main():
    """This is the main funtion of the game!"""
    print(LOGO)
    GAME_TYPE = str(input("Please select a difficulty? easy | hard: ")).lower()
    LIVES = difficulty(val=GAME_TYPE)

    number = nr_guess_value()

    your_guess = int(input("Make a guess: "))

    while LIVES != 0:
        x = hot_cold(number_to_guess=number, guess=your_guess)
        if isinstance(x, int):
            webbrowser.open(LINK)
            break
        print(PRINT_BREAKER)
        LIVES -= 1
        print(f"You now have {LIVES} lives left")
        your_guess = int(input("Make another guess: "))


if __name__ == "__main__":
    main()
