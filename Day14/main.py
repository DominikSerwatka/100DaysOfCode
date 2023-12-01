import random
from game_data import data
from art import logo, vs
from clear import clear



def rand_element(person):
    element = random.choice(data)
    if not person == '':
        while person['name'] == element['name']:
            element = random.choice(data)
    return element

def who_is_higher(person_A, person_B):
    if person_A['follower_count'] >= person_B['follower_count']:
        return "a"
    else:
        return "b"
    
def format_data(person):
    """Format the account data into printable format."""
    return f"{person['name']}, a {person['description']}, from {person['country']} "

def game():
    score = 0
    person_A = rand_element('')
    person_B = rand_element(person_A)
    run = True
    print(logo)
    while run:
        
        print(f"Compare A: {format_data(person_A)}")
        print(vs)
        print(f"Compare B: {format_data(person_B)}")
        
        char = input("Who has more followers? Type 'A' or 'B': ").lower()
        if char == who_is_higher(person_A, person_B):
            score +=1
            clear()
            print(logo)
            print(f"You're right! Current score: {score}")
            person_A = person_B
            person_B = rand_element(person_A)
        else:
            run = False
            print(f"Sory, that's wrong. Final score: {score}")

game()