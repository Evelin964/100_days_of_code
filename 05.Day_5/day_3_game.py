import random
import string

print("Welcome to the PyPassword Generator!")
nr = int(input("How many letters would you like in your password?\n"))
sim = int(input("How many symbols would you like?\n"))
n = int(input("How many numbers would you like?\n"))

list_numbers = []
list_simbol = []
list_litere = []
parola = []


for x in range(0, n):
    numere = random.choice(string.digits)
    list_numbers.append(numere)


for x in range(0, sim):
    simbols = random.choice(string.punctuation)
    list_simbol.append(simbols)

empty = nr - int(len(list_numbers)) - int(len(list_simbol))

for x in range(0, empty):
    litere = random.choice(string.ascii_letters)
    list_litere.append(litere)

parola.extend([*list_litere])
parola.extend([*list_simbol])
parola.extend([*list_numbers])

random.shuffle(parola)
parola_string = ""
parola_string = "".join(parola)


print(f"Here is your password: {parola_string}")
