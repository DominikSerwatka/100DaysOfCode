# hangman mini-game

import random
from clear_console import clear
from hangman_art import stages, logo
from hangman_words import word_list

word = random.choice(word_list)

# print(f"Paast, the solution is {word}")

display = []

for str in word:
    display.append("_")


end_of_game = False

lives = 6
nr_stage = 0

print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")
    else:
        for x in range(len(word)):
            if guess == word[x]:
                display[x] = guess
                
    if guess not in word:
        lives -=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        nr_stage +=1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[nr_stage])


