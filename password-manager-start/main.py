from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- Global Variables ------------------------------- #
LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "1234567890"
special_characters = "!#$%&()*+"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password = ""
    for i in range(10):
        number = random.randint(1, 3)
        if number == 1:
            password += random.choice(LETTERS)
        elif number == 2:
            password += random.choice(NUMBERS)
        else:
            password += random.choice(special_characters)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def delete_success():
    success.config(text="")


def save():
    website_ent = website_entry.get()
    emai_ent = email_user_entry.get()
    password_ent = password_entry.get()

    if (len(website_ent) == 0) or (len(password_ent) < 0) or (len(emai_ent) < 0):
        messagebox.showerror(title="WHOOPSIE DOOPSIE", message="Please don't leave any of the fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_ent, message=f"These are the info entered:\nEmail: {emai_ent}"
                                                                  f"\n Password: {password_ent}"
                                                                  f"\nIs it ok to save?")
        if is_ok:
            success.config(text="Success! data saved :)")
            with open("/Users/khaspper/Documents/data.txt", mode="a") as password_file:
                password_file.write(f" {website_ent} | {emai_ent} | {password_ent}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            window.after(2500, delete_success)


# ---------------------------- UI SETUP ------------------------------- #
# * Making the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# * Setting up the Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_IMG = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_IMG)
canvas.grid(column=1, row=1)

# * Creating the Website label and text entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=2)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=2, columnspan=2)
website_entry.focus()

# * Creating the Email/Username Entries
email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=3)

email_user_entry = Entry(width=35)
email_user_entry.insert(0, "brandonnarciso24@gmail.com")
email_user_entry.grid(column=1, row=3, columnspan=2)

# * Creating the Password Entry
password_label = Label(text="Password:")
password_label.grid(column=0, row=4)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=4)

genPassword_button = Button(text="Generate Password", width=11, command=generate_password)
genPassword_button.grid(column=2, row=4)

# * Creating the Add button
add_info = Button(text="Add", width=34, command=save)
add_info.grid(column=1, row=5, columnspan=2)

# * Creating a Success text when the Data has been added to the data file
success = Label(fg="#9bdeac")
success.grid(column=1, row=0)

window.mainloop()
