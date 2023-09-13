"""This game_on is a treasure island game_on with options to choose from!
"""


design_lines = [
    "    *******************************************************************************",
    "             |                   |                  |                     |",
    '    _________|________________.=""_;=.______________|_____________________|_______',
    '    |                   |  ,-"_,=""     `"=.|                  |',
    '    |___________________|__"=._o`"-._        `"=.______________|_________________',
    '            |                `"=._o`"=._      _`"=._                     |',
    '    ________|_____________________:=._o "=._."_.-="\'"=.__________________|_______',
    '    |                   |    __.--" , ; `"=._o." ,-"""-._ ".      |',
    '    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". \'_____|______________',
    '            |             |o`"=._` , "` `; .". ,  "-._"-._; ;                |',
    '    ________|_____________| ;`-.o`"=._; ." ` \'`."\\` . "-._ /_________________|_____',
    '    |                   | |o;    `"-.o`"=._``  \'` " ,__.--o;   |',
    '    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________',
    '    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____',
    '    /______/______/______/"=._o--._        ; | ;        ; ;/______/______/______/__',
    '    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____',
    '    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/',
    '    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____',
    "    /______/______/______/______/______/______/______/______/______/______/_____ /",
    "    *******************************************************************************",
]

for line in design_lines:
    print(line)

print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")

game = True

while game:
    first_choice = input(
        'You are at a cross road. Where do you want to go? Type "left" or "right" '
    )
    if first_choice == "right":
        print("You fell into a hole. Game Over.")
        again = input("Would you like to play again ? Y | N ")
        if again.upper() == "Y":
            continue
        else:
            game = False
    elif first_choice == "left":
        second_choice = input(
            "You've come to a lake."
            ' There is an island in the middle of the lake. Type "wait"'
            ' to wait for a boat. Type "swim" to swim across. '
        )
        if second_choice == "swim":
            print("You get attacked by an angry trout. Game Over.")
            again = input("Would you like to play again ? Y | N ")
            if again.upper() == "Y":
                continue
            else:
                game = False
        elif second_choice == "wait":
            third_choice = input(
                "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? "
            )
            if third_choice == "red":
                print("It's a room full of fire. Game Over.")
                again = input("Would you like to play again ? Y | N ")
                if again.upper() == "Y":
                    continue
                else:
                    game = False
            elif third_choice == "blue":
                print("You enter a room of beasts. Game Over.")
                again = input("Would you like to play again ? Y | N ")
                if again.upper() == "Y":
                    continue
                else:
                    game = False
            elif third_choice == "yellow":
                print("You found the treasure you win!")
                again = input("Would you like to play again ? Y | N ")
                if again.upper() == "Y":
                    continue
                else:
                    game = False
            else:
                again = input("Wrong choice, would you like to play again ? Y | N ")
                if again.upper() == "Y":
                    continue
                else:
                    game = False
        else:
            again = input("Wrong choice, would you like to play again ? Y | N ")
            if again.upper() == "Y":
                continue
            else:
                game = False
