import pandas
import random
from tkinter import *


# ---------------------- FUNCTIONS ---------------------- #
def known_words():
    pandas.DataFrame.from_records(foreign_words).to_csv("words_to_learn.csv")
    random_word()

def flip_card():
    global learn_word
    english_word = foreign_words[index]["English"]
    del foreign_words[index]
    card.itemconfig(color_of_card, image=back_card_IMG)
    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(card_bottom, text=english_word, fill="white")


def random_word():
    global index, flip_timer
    window.after_cancel(flip_timer)
    index = random.randint(0, len(foreign_words) - 1)
    new_word = foreign_words[index]["French"]
    card.itemconfig(color_of_card, image=front_card_IMG)
    card.itemconfig(card_title, text="French", fill="black")
    card.itemconfig(card_bottom, text=new_word, fill="black")
    flip_timer = window.after(3000, flip_card)


# ---------------------- GLOBAL VARIABLES ---------------------- #
learn_word = False
words_to_learn = []
index = 0
BACKGROUND_COLOR = "#B1DDC6"
try:
    foreign_words_csv = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    foreign_words_csv = pandas.read_csv("data/french_words.csv")

foreign_words = foreign_words_csv.to_dict(orient="records")
print(foreign_words)

# * Making the window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
flip_timer = window.after(3000, flip_card)

# * Making the Flash card
card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_IMG = PhotoImage(file="images/card_front.png")
back_card_IMG = PhotoImage(file="images/card_back.png")
color_of_card = card.create_image(400, 263, image=front_card_IMG)
card.grid(column=0, row=0, columnspan=2)
card_title = card.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
card_bottom = card.create_text(400, 263, font=("Ariel", 60, "bold"), fill="black")

# * Making the buttons
wrong_IMG = PhotoImage(file="images/wrong.png")
red_button = Button(image=wrong_IMG, highlightthickness=0, command=random_word)
red_button.grid(column=0, row=1)

right_IMG = PhotoImage(file="images/right.png")
green_button = Button(image=right_IMG, highlightthickness=0, command=known_words)
green_button.grid(column=1, row=1)

random_word()
window.mainloop()
