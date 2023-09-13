"""
    This program tells you how much you have to pay and what tip would you like to give
"""

print("Welcome to the tip calculator.")
bill = input("What was the total bill?: ")
ppl = input("How many people to split the bill?: ")
tip = input("what percentage tip would you like to give? 10%, 12%, or 15%: ")

total = float(bill) / int(ppl) + int(tip) * (float(bill) / int(ppl)) / 100

print(f"Each person should pay: {total}")
