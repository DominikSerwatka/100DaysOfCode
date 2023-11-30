# The Number Guessing Game
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5



def generate_number():
    number = randint(1, 100)
    return number

def check_number(user_guess, number):
    """Checks user guess against answer. Returns 0 if answer is right nad none if incorrect."""
    if user_guess == number:
        print(f"You got it! The answer was {user_guess}.")
        return 0
    elif user_guess>number:
        print("To high.") 
        return
    else:
        print("To low.") 
        return
    
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    number = generate_number()
    print(number)
    if dificulty == 'easy':
        number_of_attempts = EASY_LEVEL
    elif dificulty == 'hard':
        number_of_attempts = HARD_LEVEL

    run = True
    while number_of_attempts != 0 and run == True:
        print(f"You have {number_of_attempts} attemps remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        number_of_attempts -= 1
        if check_number(user_guess, number) == 0:
            run = False
        elif number_of_attempts == 0:
            print(f"You lose. The answer was {number}")
        else:
            print("Guess again.")

game()

