from art import logo
from clear_console import clear

print(logo)

print("Welcome to the secret auction program.")

bid_dictionary = {}

def add_new_bid(name, bid):
    bid_dictionary[name] = bid

def who_won():
    max = 0
    winner_name = ""
    for str in bid_dictionary:
        dollars = bid_dictionary[str]
        if dollars > max:
            max = dollars
            winner_name = str
    print(f"The winner is {winner_name} with a bid of ${max}")

run = True
while run:
    name = input("What is your name?: ")
    bid = int(input("what's your bid?: $"))
    add_new_bid(name, bid)
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if answer == "no":
        clear()
        who_won()
        run = False
    else:
        clear()
