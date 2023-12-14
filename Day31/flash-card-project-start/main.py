from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


try:
    data = pandas.read_csv("data/french_words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")


current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=img_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=img_back)


def is_known():
    to_learn.remove(current_card)
    write_to_csv(to_learn)
    next_card()


def write_to_csv(data):
    data_frame = pandas.DataFrame(data)
    data_frame.to_csv("data/french_words_to_learn.csv", index=False)


# ---- UI SETUP ----- #

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
img_front = PhotoImage(file="images/card_front.png")
img_back = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 268, image=img_front)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, "bold"))

my_image_yes = PhotoImage(file="images/right.png")
button_yes = Button(image=my_image_yes, highlightthickness=0, command=is_known)

my_image_no = PhotoImage(file="images/wrong.png")
button_no = Button(image=my_image_no, highlightthickness=0, command=next_card)

button_yes.grid(column=0, row=1, pady=10)
button_no.grid(column=1, row=1, pady=10)

next_card()


window.mainloop()
