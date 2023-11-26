import random
letters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-']

print("Welcome to the PyPassward Generator!")
nr_letter = int(input("How many letter would you like in your passward?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

sum = nr_letter+nr_numbers+nr_symbols

passward_letter = ""

for x in range(0, nr_letter):
    passward_letter += random.choice(letters)

passward_symbol = ""

for x in range(0, nr_symbols):
    passward_symbol += random.choice(symbols)

passward_number = ""

for x in range(0, nr_numbers):
    passward_number += random.choice(numbers)

passward = passward_letter+passward_number+passward_symbol

passward_list = [*passward]
y = 0
help = ""

for x in range(0, sum):
    random_number = random.randint(0, sum-1)
    help = passward_list[y]
    passward_list[y] = passward_list[random_number]
    passward_list[random_number] = help
    y += 1

passward = ""

passward = passward.join(passward_list)

print(f"Your passward is : {passward}")

random.shuffle(passward_list)
passward = ""
passward = passward.join(passward_list)
print(f"Your passward using \'shuffle()\' function is : {passward}")


    
