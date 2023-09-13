from day_15_art import coffee_data, initial_resources
import sys


class CoffeeMachine:
    """This Class is a coffee machine with all the functionality"""

    def __init__(self, resources: dict, coffee_options: dict, coins=0):
        """This is the init method of the class coffe_machine

        Args:
            resources (dict): It's the things it requires to make coffee.
            coffee_options (dict): The coffee things it can make.
            coins (int, optional): Its the money it has inside. Defaults to 0.
        """
        self.resources = resources
        self.coffee_options = coffee_options
        self.coins = coins

    def your_coffee_choices(self) -> str:
        choice = input("What would you like to drink today my friend?: ")
        return choice

    def report(self):
        """This method generates a report with the remaining resources available inside the machine."""
        for resource, quantity in self.resources.items():
            print(f"-- {resource}: {quantity} --")

    def coffee_offerings(self) -> str:
        offerings = " | ".join(
            [
                f"{coffee} (${self.coffee_options[coffee]['cost']:.2f})"
                for coffee in self.coffee_options.keys()
            ]
        )
        return offerings

    def turning_off(self):
        """Exists the program aka closes the machine."""
        print("Turning Off! Goodbye")
        sys.exit()

    def check_resources(self, choice: str) -> bool:
        # verifica resurse si are nevoie de cafeaua aleasa
        """Checks for the resources based on your choice.
        Args:
            choice (str): Takes in your choice made in the prompt method.
        Returns:
            bool: Makes your coffee or not based on the resources.
        """
        if choice not in self.coffee_options:
            print("Invalid Choice. Please choose from the available options.")
            return False
        for resource, quantity_required in self.coffee_options[choice][
            "ingredients"
        ].items():
            if quantity_required > self.resources.get(resource, 0):
                print(f"Insufficient {resource}. Cannot make {choice}")
                return False
        return True

    def check_coins(self, choice, coins):
        if self.coffee_options[choice]["cost"] > coins:
            return False
        else:
            return True

    def making_coffee(self, choice: str) -> dict:
        # face cafeaua adica scade din resursele introduse costul cafelei tale
        """Makes the actual coffee.

        Args:
            choice (str): Takes in your choice and makes your coffee
        """
        for resource, quantity_required in self.coffee_options[choice][
            "ingredients"
        ].items():

            return self.resources[resource] - quantity_required

    def money_inserted(self) -> int:
        # returneaza coins pe care le-ai bagat in aparat
        """This is the balances(money) aka register

        Args:
            required_ammount (int): The ammount required to make the coffee.

        Returns:
            int: Your change.
        """

        # quarters = 25 cents
        quarters = float(input("Please input how many quarters (25 cents): "))
        # dimes = 10 cents
        dimes = float(input("Please input how many dimes (10 cents): "))
        # nikel = 5 cents
        nickel = float(input("Please input how many nickels (5 cents): "))
        # penni = 1 cent
        penni = float(input("Please input how many pennies (1 cents): "))
        self.coins = quarters * 0.25 + dimes * 0.10 + nickel * 0.05 + penni * 0.01
        return self.coins


cafea = CoffeeMachine(coffee_options=coffee_data, resources=initial_resources)

# resursa = cafea.making_coffee(choice="latte")
# coins_inserted = cafea.money_inserted()
# coins_check = cafea.check_coins(choice="latte", coins=coins_inserted)

# check_resursa = cafea.check_resources(choice="latte")
cafea.report()

fa_cafea = cafea.making_coffee(choice="latte", coffee_options=coffee_data)

print(fa_cafea)

cafea.report()
# print(coins_check)
# print(coins_inserted)
