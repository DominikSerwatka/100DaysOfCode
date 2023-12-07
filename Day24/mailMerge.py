#TODO: Create a letter using starting_letter.txt


#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt", mode="r") as file:
    name_list = file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    first_line_of_latter = file.readline()
    letter = file.read()

for item in name_list:
    item = item.strip()
    list_final = first_line_of_latter.replace("[name]", item)
    with open(f"./Output/ReadyToSend/letter_for_{item}.txt", mode="w") as file:
        file.write(list_final+letter)



