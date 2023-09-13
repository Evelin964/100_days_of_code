"""This is a BlackJack game for my day 11 project
    This is the testing file that i made to check if everything works"""


# =====================================================================#
#                          Imports                                     #
import random
import webbrowser
import time

##===========================================================##
## - art
## - try stuff

CARDS = [
    "2H",
    "3H",
    "4H",
    "5H",
    "6H",
    "7H",
    "8H",
    "9H",
    "10H",
    "JH",
    "QH",
    "KH",
    "AH",
    "2D",
    "3D",
    "4D",
    "5D",
    "6D",
    "7D",
    "8D",
    "9D",
    "10D",
    "JD",
    "QD",
    "KD",
    "AD",
    "2C",
    "3C",
    "4C",
    "5C",
    "6C",
    "7C",
    "8C",
    "9C",
    "10C",
    "JC",
    "QC",
    "KC",
    "AC",
    "2S",
    "3S",
    "4S",
    "5S",
    "6S",
    "7S",
    "8S",
    "9S",
    "10S",
    "JS",
    "QS",
    "KS",
    "AS",
]

LINK = "https://www.instagram.com/reel/Cs-7mUzrn3e/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="


# =========================== Def zone =================================#


def hands(n):
    hand = []
    for _ in range(n):
        random.shuffle(CARDS)
        x = random.choice(CARDS)
        CARDS.remove(x)
        hand.append(x)
    return hand


def check_hand(hand):
    points = 0
    aces = 0
    for card in hand:
        rank = card[:-1]
        if rank.isdigit():
            points += int(rank)
        elif rank in ["J", "Q", "K"]:
            points += 10
        elif rank == "A":
            aces += 1
    return aces, points


def aces_logic(n):
    total_ace_value = 0

    for i in range(n):
        ace_value = int(input(f"What should be the value of Ace {i+1}?: (1 | 11) "))
        total_ace_value += ace_value

    return total_ace_value


def adjust_computer_ace_value(hand, hand_info):
    num_aces, points = hand_info

    for i in range(num_aces):
        if hand[i] == "A":
            second_card_rank = hand[i + 1][:-1]
            if second_card_rank.isdigit() and points + 11 > 21:
                hand[i] = "A1"  # Ace is worth 1 if sum with second card is over 21
            elif second_card_rank in ["10", "J", "Q", "K"]:
                hand[i] = "A1"  # Ace is worth 1 if sum is 21
    return hand


def game_logic(player_points=int, computer_points=int):
    if player_points > 21:
        print("Player Bust! Computer wins!")
    elif computer_points > 21:
        print("Computer Bust! Player wins!")
    elif player_points > computer_points:
        print("Player Wins!")
    elif computer_points > player_points:
        print("Computer Wins!")
    else:
        print("Its a tie! ")


##=============================================================##
##                      Main zone                              ##


def main():
    game = True
    comp_hand = []
    player_hand = []
    balance = 0
    while game:

        ########################################################
        print("===================================")
        if balance <= 0 and game is True:
            deposit = int(input("How much would you like to deposit? $ : "))
            balance += deposit
        #

        print(f"Your balance: {balance} $")
        # ask for bet
        bet = int(input("How much would you like to bet?: "))
        balance -= bet
        if bet > deposit:
            deposit = int(
                input(
                    f"Your bet is not enough for betting. Please add {bet - deposit} $ "
                )
            )
            balance += deposit

        print(f"Your balance is: {abs(balance)}")
        print("===================================")

        ########################################################
        if len(comp_hand) == 0 and len(player_hand) == 0:
            comp_hand = hands(2)
            player_hand = hands(2)
            if any(card in comp_hand for card in player_hand):
                comp_hand = hands(2)  # Replace the computer's hand if cards match
            if any(card in player_hand for card in comp_hand):
                player_hand = hands(2)  # Replace the player's hand if cards match

        ##################################################
        player_points = check_hand(player_hand)
        points_player = player_points[1]
        aces_player = int(player_points[0])

        ##################################################

        ##################################################
        comp_points = check_hand(comp_hand)
        points_computer = comp_points[1]
        aces_comp = int(comp_points[0])

        ##################################################
        if aces_comp > 0:
            comp_hand = adjust_computer_ace_value(comp_hand, comp_points)
            comp_points = check_hand(comp_hand)
            points_computer = comp_points[1]

        print(f"Your hand is: {player_hand} with a value of: {points_player}")
        print(f"The computers card is ['{comp_hand[0]}']")

        if aces_player > 0:
            points_player += aces_logic(aces_player)
            print(
                f"Your hand is: {player_hand} with a total value of {points_player} after Ace adjustments"
            )

        ###########################################################

        ##################################################
        print("===================================")

        # check to see if the player wants to hit or stand.
        hit = input(
            f"Your hand is {player_hand}, with a value of {points_player}  would you like to hit or stand? (Y | N) : "
        ).lower()
        while points_player < 21 and hit != "n":
            player_hand.append(hands(1)[0])
            player_points = check_hand(player_hand)
            points_player = player_points[1]
            aces_player = int(player_points[0])
            points_player += aces_logic(aces_player)
            if points_player > 21:
                # game_logic(player_points=points_player, computer_points=points_computer)
                break
            hit = input(
                f"Your hand is {player_hand}, with a value of {points_player}  would you like to hit or stand? (Y | N) : "
            ).lower()

        # prompt for answer Y | N

        # if yes
        #### add new card to the hand
        #### check for aces and prompt for value
        #### check if
        #          points < 21
        #                yes bust
        #                no continue
        #                     print hand and points
        #
        while points_computer <= 17:

            # have a while loop that keeps dealing cards before doing the logic
            comp_new_hand = comp_hand.copy()
            new_card = hands(1)[0]
            while new_card in player_hand or new_card in comp_new_hand:
                new_card = hands(1)[0]

            comp_new_hand.append(new_card)
            comp_points_tuple = check_hand(
                comp_new_hand
            )  # Get the tuple from check_hand
            comp_new_hand = adjust_computer_ace_value(comp_new_hand, comp_points_tuple)
            comp_new_points = comp_points_tuple[1]

            print(f"Computer's hand is {comp_new_hand}")
            print(f"Computers points are {comp_new_points}")
            print("=========================================")
            game_logic(player_points=points_player, computer_points=comp_new_points)
            print("===================================================")
            print(f"Your hand was {player_hand} with a value of {points_player}")
            break
        else:
            comp_points_tuple = check_hand(comp_hand)  # Get the tuple from check_hand
            comp_hand = adjust_computer_ace_value(comp_hand, comp_points_tuple)
            comp_new_points = comp_points_tuple[1]

            game_logic(player_points=points_player, computer_points=points_computer)
            print("===================================")
            print(
                f"Computer's hand is: {comp_hand} with total value of {points_computer}"
            )
            print(f"Your hand is: {player_hand} with a total value of {points_player}")

        ########################################################################

        play_again = input("Would you like to play again? (Y | N): ").lower()

        if play_again == "n":
            print("Ok! Goodbye!!")
            game = False

        elif play_again == "y" and balance > 0:
            comp_hand.clear()
            player_hand.clear()
        elif play_again == "y" and balance <= 0:
            comp_hand.clear()
            player_hand.clear()
            webbrowser.open(LINK)
            time.sleep(20)


if __name__ == "__main__":
    main()
