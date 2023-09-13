import random

print("Hello Welcome to Rock Paper Scissors")

# Define the hand models
rock = """
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
Paper
      _______
          _______)
         _______)
        _______)
       _______)
"""
scissors = """
Scissors
---'   _______
         ______)
      ____(____)
---'    (_____)
"""

choices = [rock, paper, scissors]

# Ask user for input 0 - rock 1 - paper 2 - scissors
player = int(input("Please choose between 0-Rock | 1-Paper | 2-Scissors : "))

# Validate user input
if player < 0 or player > 2:
    print("Invalid choice.")
else:
    computer = random.randint(0, 2)
    print(choices[computer])
    print(choices[player])

    # Define winning conditions
    winning_conditions = {(0, 2), (2, 1), (1, 0)}

    if (computer, player) in winning_conditions:
        print("Player won!")
    elif (player, computer) in winning_conditions:
        print("Computer won!")
    else:
        print("It's a tie!")
