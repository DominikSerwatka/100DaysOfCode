import pandas
#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
nato_list = []
for letter in word:
    nato_list.append(nato_dict[letter])
print(nato_list)

