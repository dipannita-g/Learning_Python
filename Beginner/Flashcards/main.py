import pandas
from tkinter import *
from tkinter import PhotoImage
import random

BACKGROUND_COLOR = "#B1DDC6"
TIMER = 3000

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/French-English-translations.csv")

words_to_learn = data.to_dict(orient="records")
current_card = {}

# ---------------------------- RANDOM WORD GENERATOR ------------------------------- #

def next_card():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_word, text= f"{french_word}", fill = "black")
    canvas.itemconfig(card_title, text= "French", fill = "black")
    flip_timer = window.after(TIMER, flip_card)

# ---------------------------- FLIP CARD ------------------------------- #

def flip_card():

    english_word = current_card["English"]
    canvas.itemconfig(card_img, image = card_back_img)
    canvas.itemconfig(card_word, text=f"{english_word}", fill= "white")
    canvas.itemconfig(card_title, text="English", fill= "white")

# ---------------------------- CORRECT ANSWER ------------------------------- #

def correct_answer():

    words_to_learn.remove(current_card)
    new_dict = pandas.DataFrame(words_to_learn)
    new_dict.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(TIMER, flip_card)

right_img = PhotoImage(file= "images/right.png")
wrong_img = PhotoImage(file = "images/wrong.png")
card_back_img = PhotoImage(file = "images/card_back.png")
card_front_img = PhotoImage(file= "images/card_front.png")

# Flash card
canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 300, image = card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button = Button(image=right_img, highlightthickness=0, command=correct_answer)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

# Texts
card_title = canvas.create_text(400, 170, text=f"{""}", font=("Arial", 40, "bold italic"))
card_word = canvas.create_text(400, 350, text=f"{""}", font=("Arial", 60, "bold"))

next_card()

window.mainloop()