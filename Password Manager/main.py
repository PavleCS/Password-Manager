from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

LIGHT_BLUE = "#BAD7E9"
DARK_BLUE = "#2B3467"
FONT = "Arial"
SIZE = 10
STYLE = "bold"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|', '<',
           ',', '>', '.', '?', '/']


def random_pass():
    rand_alphabet = random.choices(alphabet, k=8)
    rand_symbols = random.choices(symbols, k=8)
    rand_pass = rand_alphabet + rand_symbols
    random.shuffle(rand_pass)
    final_pass = "".join(rand_pass)
    password_entry.delete(0, END)
    password_entry.insert(0, f"{final_pass}")
    pyperclip.copy(final_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def entry_funcs():
    website = website_entry.get().lower()
    email = email_entry.get().lower()
    password = password_entry.get().lower()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("My_Passwords.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("My_Passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("My_Passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Search Funcs ------------------------------- #
def search():
    search_term = website_entry.get().lower()
    try:
        with open("My_Passwords.json", "r") as data_file:
            data = json.load(data_file)
            if search_term in data:
                file_found = data[search_term]
                messagebox.showinfo(title="Search Results:", message=f"Email: {file_found['email']} \nPassword:"
                                                                     f" {file_found['password']}")
            else:
                messagebox.showerror(title="Oops!", message="No details for the website exist! Please try again.")
    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message="Sorry, no DataFile found! Please enter some data first!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(pady=50, padx=50)
window.config(bg=LIGHT_BLUE)

# ------------------------------ Canvas ------------------------------ #
canvas = Canvas(width=200, height=200, bg=LIGHT_BLUE, highlightthickness=0)
safe_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=safe_img)
canvas.grid(column=1, row=0)

# ------------------------------ website ------------------------------ #
website_label = Label(text="Website:", font=(FONT, SIZE, STYLE), bg=LIGHT_BLUE)
website_label.grid(column=0, row=1)

website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="W")

# ------------------------------ Email/Username ------------------------------ #
email_label = Label(text="Email/Username:", font=(FONT, SIZE, STYLE), bg=LIGHT_BLUE)
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.insert(0, "lebeda.pavle@yahoo.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# ------------------------------ Password ------------------------------ #
password_label = Label(text="Password:", font=(FONT, SIZE, STYLE), bg=LIGHT_BLUE)
password_label.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="W")

# ------------------------------ Generate button ------------------------------ #
generate_button = Button(text="Generate Password", command=random_pass, font=(FONT, SIZE, STYLE),
                         bg=DARK_BLUE, fg="white")
generate_button.grid(column=2, row=3, sticky="E")

# ------------------------------ Add button ------------------------------ #
add_button = Button(text="Add", width=36, font=(FONT, SIZE, STYLE), command=entry_funcs, bg=DARK_BLUE, fg="white")
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

# ---------------------------- Search ------------------------------- #
search_button = Button(text="Search", font=(FONT, SIZE, STYLE), bg=DARK_BLUE, fg="white", command=search)
search_button.grid(column=2, row=1, sticky="EW")


window.mainloop()
