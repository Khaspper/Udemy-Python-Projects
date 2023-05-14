from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
def search():
    website_to_search = website_entry.get().lower()
    try:
        with open("/Users/khaspper/Documents/data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website_to_search in data:
            messagebox.showinfo(title=website_to_search, message=f"Email/Username: {data[website_to_search]['email']}\n"
                                                                 f"\nPassword: {data[website_to_search]['password']}")
        else:
            messagebox.showerror(title="WHOOPSIE DAISY", message=f"No details for the website "
                                                                 f'"{website_to_search.title()}" exists.')


def delete_success():
    success.config(text="")


def save():
    website_ent = website_entry.get().lower()
    emai_ent = email_user_entry.get()
    password_ent = password_entry.get()
    new_data = {
        website_ent: {
            "email": emai_ent,
            "password": password_ent,
        }
    }

    if (len(website_ent) == 0) or (len(password_ent) < 0) or (len(emai_ent) < 0):
        messagebox.showerror(title="WHOOPSIE DOOPSIE", message="Please don't leave any of the fields empty!")
    else:
        success.config(text="Success! data saved :)")
        try:
            with open("/Users/khaspper/Documents/data.json", mode="r") as password_file:
                # * Reading old data
                data = json.load(password_file)
        except FileNotFoundError:
            with open("/Users/khaspper/Documents/data.json", mode="w") as password_file:
                # * Saving updated data
                json.dump(new_data, password_file, indent=4)
        else:
            # * Updating old data with new data
            data.update(new_data)
            with open("/Users/khaspper/Documents/data.json", mode="w") as password_file:
                # * Saving updated data
                json.dump(data, password_file, indent=4)
        finally:
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

website_entry = Entry(width=20)
website_entry.grid(column=1, row=2)
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

# * Creating the search button
search_button = Button(text="Search", width=11, command=search)
search_button.grid(column=2, row=2)

window.mainloop()
