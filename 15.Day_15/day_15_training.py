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
        self.choice = None
        self.offerings = None
        ## aici help pls
        self.resource = None
        self.quantity_required = None

    def your_coffee_choices(self) -> None:
        """Asks you for what would you like to drink."""
        self.choice = input("What would you like to drink today my friend?: ")

    def report(self):
        """This method generates a report with the remaining resources available inside the machine."""
        for resource, quantity in self.resources.items():
            print(f"-- {resource}: {quantity} --")

    def coffee_offerings(self) -> None:
        """This method show you the offerings ofthe coffe machine in a dinamic way."""
        self.offerings = " | ".join(
            [
                f"{coffee} (${self.coffee_options[coffee]['cost']:.2f})"
                for coffee in self.coffee_options.keys()
            ]
        )
        print(self.offerings)

    def turning_off(self):
        """Exists the program aka closes the machine."""
        print("Turning Off! Goodbye")
        sys.exit()

    def check_resources(self) -> bool:
        """Checks for the resources based on your choice.
        Args:
            choice (str): Takes in your choice made in the prompt method.
        Returns:
            bool: Makes your coffee or not based on the resources.
        """
        if self.choice not in self.coffee_options:
            print("Invalid Choice. Please choose from the available options.")
            return False
        else:
            for self.resource, self.quantity_required in self.coffee_options[
                self.choice
            ]["ingredients"].items():
                if self.quantity_required > self.resources.get(self.resource, 0):
                    print(f"Insufficient {self.resource}. Cannot make {self.choice}")
                else:
                    return True

    def check_coins(self) -> bool:
        return self.coffee_options[self.choice]["cost"] > self.coins

    def making_coffee(self) -> dict:
        """Makes the actual coffee.
        Args:
            choice (str): Takes in your choice and makes your coffee
        """
        for resource, quantity_required in self.coffee_options[self.choice][
            "ingredients"
        ].items():
            self.resources[resource] = self.resources[resource] - quantity_required

    def money_inserted(self) -> int:

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

    def coffee_brain(self):
        """This is the main brain calling all methods and does all the doing."""
        while True:

            if self.coins == 0:
                self.coffee_offerings()
                self.your_coffee_choices()
                if self.choice == "off":
                    self.turning_off()
                elif self.choice == "report":
                    self.report()
                    self.turning_off()
                self.money_inserted()

                if self.check_resources() is True:
                    self.making_coffee()

                    print(
                        f"Here is your {self.choice}☕😊 Enjoy! You have {self.coins} left."
                    )
                    self.coins -= self.coffee_options[self.choice]["cost"]
                ### aici nu printeazza
            elif self.coins > 0:
                self.coffee_offerings()
                self.your_coffee_choices()
                if self.choice == "off":
                    self.turning_off()
                elif self.choice == "report":
                    self.report()
                    self.turning_off()

                if self.check_resources() is True:
                    self.making_coffee()
                    print(
                        f"Here is your {self.choice}☕😊 Enjoy! You have {self.coins} left."
                    )
                    self.coins -= self.coffee_options[self.choice]["cost"]
                ### si aici la fel

            elif self.choice == "off":
                self.turning_off()
            elif self.choice == "report":
                self.report()


cafea = CoffeeMachine(resources=initial_resources, coffee_options=coffee_data)

cafea.coffee_brain()
