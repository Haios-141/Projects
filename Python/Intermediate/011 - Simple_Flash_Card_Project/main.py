import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
SECONDS = 5000
SAVED_WORDS = "data/words_to_learn.csv"

try:
    data = pandas.read_csv(SAVED_WORDS).to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/japanese_words.csv").to_dict(orient="records")

current_card = {}


def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)

    current_card = random.choice(data)

    canvas.itemconfig(card_title, text="Japanese", fill="#000")
    canvas.itemconfig(card_word, text=current_card["Japanese"], fill="#000")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(SECONDS, flip_card)


def is_known():
    data.remove(current_card)
    # print(len(data))
    save_data = pandas.DataFrame(data)
    save_data.to_csv(SAVED_WORDS, index=False)
    next_card()


def flip_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="English", fill="#fff")
    canvas.itemconfig(card_word, text=current_card["English"], fill="#fff")
    canvas.itemconfig(canvas_img, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(SECONDS, flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
