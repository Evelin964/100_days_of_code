# TODO 1 - create a class QuizzGame
# TODO 2 - resolve the interaction with the Trivia API so we can get
# - questions from either a random area or a specific area
# - by prompting the user in the begining
# TODO 3 - create a method that decodes the information so we can see it in the accuate way
# TODO 4 - create a method that stores the information after decoding
# TODO 5 - create a score keeping method for each TRUE/FALSE answer
# TODO 6 - create the brain of the game - aka the caller method
# TODO 7 - loop this bitch up


import requests
import html


link = "https://opentdb.com/api.php?amount=10&category=10&type=boolean"

rasp = requests.get(link)
print(rasp.status_code)
data = rasp.json()


print(data)
