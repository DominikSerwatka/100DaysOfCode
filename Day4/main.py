import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

game_list = [rock, paper, scissors]

print("You chose:")
print(game_list[choose])
computer_choose = random.randint(0, 2)
print("Computer chose:")
print(game_list[computer_choose])

if choose == computer_choose:
    print("Draw")
elif choose == 0:
    if computer_choose == 1:
        print("You lose")
    else:
        print("You win")
elif choose == 1:
    if computer_choose == 0:
        print("You win")
    else:
        print("You lose")
else:
    if computer_choose == 0:
        print("You lose")
    else:
        print("You win")
        

