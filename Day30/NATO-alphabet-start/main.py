import pandas
#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


#
#
# is_on = True
#
# while is_on:
#     word = input("Enter a word: ").upper()
#     nato_list = []
#     for letter in word:
#         try:
#             nato_list.append(nato_dict[letter])
#         except KeyError:
#             print("Sorry, only letters in the alphabet please.")
#             is_on = True
#             break
#         else:
#             is_on = False
#
# print(nato_list)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()

