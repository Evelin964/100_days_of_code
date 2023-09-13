"""

This is a secret aution program for day_9 project

"""

# ===================== Imports ===================================###
import os
from secret_auction_art import ASCII_LOGO


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++###

# ==================================================================#
#                    Defining stuff                                #


def clear_terminal():
    """clears terminal for each player so they wont know who bid what"""
    os.system("cls" if os.name == "nt" else "clear")


# ========================= Main =====================================#


def main():
    """Main Implementation of the game!"""
    print(ASCII_LOGO)
    all_bids = {}

    while True:
        name_input = input("Hello, please tell me your Name: ")
        bid_input = int(input("What is your bid amount: "))

        all_bids[name_input] = bid_input

        more_ppl = input("Are there any more bidders? (Y/N): ").lower()

        if more_ppl == "n":
            max_bidder = max(all_bids, key=all_bids.get)
            max_bid = all_bids[max_bidder]
            clear_terminal()
            print(ASCII_LOGO)
            print(f"The biggest bidder is {max_bidder} with a bid of {max_bid}!")
            break
        elif more_ppl == "y":
            clear_terminal()
            print(ASCII_LOGO)


if __name__ == "__main__":
    main()
