"""This is the Day 17 project for my 100 days 100 projects cource by Angela Yu
    THe missing days 16 is done inside the day 15 folder.
    """
import random
import html
import requests


class QuizzGame:
    """This is the Main Class for the Quizz Game."""

    def __init__(self):
        self.api_url = "https://opentdb.com/api.php"
        self.category_url = "https://opentdb.com/api_category.php"
        self.categories = {}
        self.category_choice = None  # Store the user's category choice
        self.custom_to_api_mapping = {}  # Mapping from custom keys to API category IDs
        self.api_to_custom_mapping = {}  # Mapping from API category IDs to custom keys
        self.questions = []
        self.correct_answers = 0  # Initialize correct answers count
        self.total_questions = 0  # Initialize total questions count

    def get_categories(self):
        """Gets all the categories from the OpenTriviaDB API."""
        # Fetch the category list from the API
        response = requests.get(self.category_url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            self.categories = {
                category["id"]: category["name"]
                for category in data["trivia_categories"]
            }
            print("Available Categories:")
            for i, (category_id, category_name) in enumerate(
                self.categories.items(), start=1
            ):
                self.custom_to_api_mapping[
                    i
                ] = category_id  # Custom key to API ID mapping
                self.api_to_custom_mapping[
                    category_id
                ] = i  # API ID to custom key mapping
                print(f"{i}: {category_name}")
        else:
            print("Failed to retrieve categories from the API")

    def ask_category_choice(self):
        """Gets your category from where you want to be quizzed. Random or Specific."""
        print("Welcome to the Quiz Game!")

        # Fetch the categories regardless of the choice
        self.get_categories()

        # Ask the user if they want a specific category or random questions
        choice = input("Would you like a specific category? (yes/no): ").lower()

        if choice == "yes":
            # Ask the user for a category number (custom key)
            category_number = input("Enter the category number (1 - end): ")

            try:
                category_number = int(category_number)
                if category_number in self.custom_to_api_mapping:
                    self.category_choice = self.custom_to_api_mapping[
                        category_number
                    ]  # Get the API category ID
                    self.get_questions(
                        self.category_choice
                    )  # Fetch questions for the chosen category
                else:
                    print("Invalid category number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "no":
            # Randomly select a category ID from the custom keys
            random_key = random.choice(list(self.custom_to_api_mapping.keys()))
            self.category_choice = self.custom_to_api_mapping[random_key]
            self.get_questions(self.category_choice)  # Fetch random category questions
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    def get_questions(self, category_id):
        """Gets the questions from the api based on your category choice.

        Args:
            category_id (int): the int value mapped by the 2 dicts in the class api - mapp | mapp - api
        """
        if category_id == "":
            category_id = ""  # Empty category ID for random questions

        # Fetch questions for the specified category or random questions with a timeout
        try:
            response = requests.get(
                f"{self.api_url}?amount=10&category={category_id}&type=boolean",
                timeout=10,
            )

            if response.status_code == 200:
                data = response.json()
                self.questions = data["results"]
                self.total_questions = len(self.questions)

                # decode the question
                for question in self.questions:
                    question["question"] = html.unescape(question["question"])

            else:
                print("Failed to retrieve questions from the API")
        except requests.exceptions.Timeout:
            print("API request timed out. Please try again later.")

    def start_game(self):
        """This is the brain of the class handling all the calls and logic."""
        if self.category_choice == "":
            print("You chose random questions.")
            # Add code here to handle random questions
        elif isinstance(self.category_choice, int):
            print(
                f"You chose category {self.api_to_custom_mapping[self.category_choice]}."
            )
            # Add code here to handle specific category questions
            if self.questions:
                for index, question in enumerate(self.questions, 1):
                    print(
                        f"Question {index} [{self.correct_answers}/{self.total_questions}]: {question['question']}"
                    )
                    # Display options and handle user input for each question
                    user_answer = input("Enter 'True' or 'False': ").strip().lower()
                    if user_answer == question["correct_answer"].strip().lower():
                        print("Correct!")
                        self.correct_answers += 1
                    else:
                        print("Incorrect.")
            else:
                print("No questions available for this category.")
        else:
            print("Please choose a category first.")


if __name__ == "__main__":
    while True:
        game = QuizzGame()
        game.ask_category_choice()
        print(game.categories)
        print(game.api_to_custom_mapping)
        print(game.custom_to_api_mapping)
        game.get_questions(game.category_choice)
        game.start_game()
        play_again = input("Would you like to play again? (Yes | No?)").lower()
        if play_again != "yes":
            break
