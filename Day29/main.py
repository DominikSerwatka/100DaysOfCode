from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_list+symbols_list+numbers_list
    random.shuffle(password_list)
    password = "".join(password_list)
    entry_passward.insert(index=0, string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def button_add_clicked():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_passward.get()
    if not (len(website) != 0 and len(email) != 0 and len(password)):
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            entry_website.delete(0, 'end')
            entry_email.delete(0, 'end')
            entry_passward.delete(0, 'end')
            with open("passward.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Passward Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)


label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_passward = Label(text="Password:")
label_passward.grid(column=0, row=3)

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2, sticky="ew")
entry_website.focus()

entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2, sticky="ew")
entry_email.insert(index=0, string="dominik@gmail.com")

entry_passward = Entry(width=21)
entry_passward.grid(column=1, row=3, sticky="ew")

button_passward = Button(text="Generate Password", command=generate_password)
button_passward.grid(column=2, row=3)

button_add = Button(text="Add", width=46, command=button_add_clicked)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()
