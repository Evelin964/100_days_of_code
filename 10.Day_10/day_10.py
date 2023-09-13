"""
This is a calculator app for my Day 10 project


"""

# =====================================================================#
#                          Imports                                     #

from calculator_art import LOGO


# =========================== Def zone =================================#


def calculator(first_nr=int, second_nr=int, operation=str):
    """

    Args:
        first_nr (Integer): Your first number. Defaults to int.
        second_nr (Integer): Your second number. Defaults to int.
        operation (String): The operation you want. Defaults to str.

    Returns:
        _type_: _description_
    """
    if operation == "+":
        return first_nr + second_nr
    elif operation == "-":
        return first_nr - second_nr
    elif operation == "*":
        return first_nr * second_nr
    elif operation == "/":
        return first_nr / second_nr
    else:
        return "Invalid Operation"


# =====================================Main zone==========================#


def main():
    """This function is the Main Calculator function.
    Will return your result based on the numbers and operation provided by input."""
    print(LOGO)
    calculate_again = "y"
    result = 0  # Initialize the result to keep track of the ongoing calculation

    while calculate_again == "y":
        if result == 0:
            first_number = int(input("Please enter the first number: "))
        else:
            first_number = result  # Use the previous result as the first number
        operation = input("What would be the operation? | + | - | * | / | : ").lower()
        second_number = int(input("Please provide the next number: "))
        result = calculator(
            first_nr=first_number, second_nr=second_number, operation=operation
        )
        print(f"The result is: {result}")
        calculate_again = input(
            "Would you like to calculate some more? (Y | N): "
        ).lower()


if __name__ == "__main__":
    main()
