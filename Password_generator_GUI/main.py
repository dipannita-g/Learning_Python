from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import random
import pyperclip

BACKGROUND= "#DFD3C3"
HIGHLIGHT = "#C5705D"
BUTTON = "#D0B8A8"
FONT = ("Arial", 8, "bold")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    new_letters = [random.choice(letters) for _ in range(random.randint(6, 10))]
    new_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    new_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = new_letters + new_symbols + new_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    field_empty = False

    if len(website) < 1 or len(email) < 1 or len(password) < 1 :
        field_empty = True
        messagebox.showinfo(title="ERROR", message="Please fill in all the fields.")

    if not field_empty:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n"
                                                  f"Password: {password} \nWant to save these details?")
        if is_ok:
            with open("my_passwords.txt", "a") as data_file:
                data_file.write(f"{website}, {email}, {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BACKGROUND)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:",bg=BACKGROUND, font=FONT)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg=BACKGROUND, font=FONT)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg=BACKGROUND, font=FONT)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
website_entry.config(highlightthickness=2, highlightcolor=HIGHLIGHT)

email_entry = Entry()
email_entry.insert(END, "example@xyz.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.config(highlightthickness=2, highlightcolor=HIGHLIGHT)

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")
password_entry.config(highlightthickness=2,highlightcolor=HIGHLIGHT)

# Buttons
generate_button = Button(text="Generate Password", font=FONT, bg = BUTTON, command=generate_password)
generate_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", font=FONT, bg = BUTTON, command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
