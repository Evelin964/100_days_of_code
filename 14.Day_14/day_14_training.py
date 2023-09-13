import random
from day_14_art import data, logo, vs

# Function to get an item from the list
def get_item(val: list) -> dict:
    """Gets a dictionary from a list

    Args:
        val (list): takes in the list of dictionaries

    Returns:
        dict: a random item from the list of dictionaries
    """
    item = random.choice(val)
    val.remove(item)
    if len(val) == 0:
        print("You ran out of things to compare!")
    return item


# Function to get values from an item
def get_value_two(val: dict) -> tuple:
    """Gets the value from a dictionary that has 4 key-value pairs

    Args:
        val dict: a dictionary with 4 key-value pairs

    Returns:
        tuple: 4 values that are stored in the dictionary
    """
    follower_count = val.get("follower_count")
    name_value = val.get("name")
    description_value = val.get("description")
    country_value = val.get("country")
    return follower_count, name_value, description_value, country_value


# Function for the game logic
def game_logic(player_one_value=int, player_two_value=int, player_input=str) -> tuple:
    """This function is the main logic of the game

    Args:
        player_one_value (int, optional): Takes in the nr of followers for player 1. Defaults to int.
        player_two_value (int, optional): Takes in the nr of followers for player 2. Defaults to int.
        player_input (int, optional): Take's in your input to check if you are right. Defaults to str.

    Returns:
        tuple: A tuple containing the value (score) 0/1 and the player answer
    """
    val = 0
    player = ""
    if player_one_value > player_two_value and player_input == "a":
        val += 1
        player = "A"
        print(
            f"You're right! Player A does have more followers {follower_one_result} vs {follower_two_result}"
        )
    elif player_one_value < player_two_value and player_input == "b":
        val += 1
        player = "B"
        print(
            f"You're right! Player B does have more followers {follower_one_result} vs {follower_two_result}"
        )
    else:
        print("Sorry, that's wrong.")
        player = None
    return (val, player)


# Initialize variables
# score = 0
NR_WON_GAMES = 0
item1 = get_item(data)
item2 = get_item(data)

while True:

    # Get values for the current items

    (
        follower_one_result,
        name_one_result,
        description_one_result,
        country_one_result,
    ) = get_value_two(item1)
    (
        follower_two_result,
        name_two_result,
        description_two_result,
        country_two_result,
    ) = get_value_two(item2)

    print(logo)
    print(
        f"Compare A: {name_one_result} - a {description_one_result} from {country_one_result}"
    )
    print(vs)
    print(
        f"Against B: {name_two_result} - a {description_two_result} from {country_two_result}"
    )

    YOUR_CHOICE = str(input("Who has more followers? Type a or b: ")).lower()

    score = game_logic(
        player_one_value=follower_one_result,
        player_two_value=follower_two_result,
        player_input=YOUR_CHOICE,
    )

    # Update the number of won games
    NR_WON_GAMES += score[0]
    print("=========================================================")
    print(f"The number of won games is {NR_WON_GAMES}")
    print("=========================================================")
    if score[0] == 0:
        break
    elif score[0] == 1 and score[1] == "A":
        # Determine the next winner

        # item1 = item2.copy()
        del item2
        item2 = get_item(data)
        print(f"branch A value the values is {item2}")

    elif score[0] == 1 and score[1] == "B":
        item1 = item2.copy()
        del item2
        item2 = get_item(data)
        print(f"Branch B value the item is {item2}")

    print(f"number of remaining items in list is {len(data)}")
