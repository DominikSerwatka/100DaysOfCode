# Ceasar Cipher
from ceasar_cipher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

# first try with two speparate function
def encrypt(plain_text, shift_amount):
    code = ""
    for char in plain_text:
        index = alphabet.index(char)
        code += alphabet[(index+shift_amount)%len(alphabet)]
    print(f"The code text is {code}")

def decrypt(plain_text, shift_amount):
    code = ""
    for char in plain_text:
        index = alphabet.index(char)
        code += alphabet[(index-shift_amount)%len(alphabet)]
    print(f"The decode text is {code}")

# final function that do decode and code
def ceaser(plain_text, shift_amount, cipher_direction):
    x = 1
    if cipher_direction == "decode":
        x = -1
    code = ""
    for char in plain_text:
        if char not in alphabet:
            code += char
        else:
            index = alphabet.index(char)
            code += alphabet[(index+x*shift_amount)%len(alphabet)]
    print(f"The {cipher_direction} text is {code}")

run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)
    text = input('Type "yes" if you want to go again. Otherwise type "no".\n' )
    if text == "no":
        run = False
        print("Goodbey.")
