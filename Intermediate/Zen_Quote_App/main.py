from tkinter import *
import requests
from PIL import Image, ImageTk

BACKGROUND_COLOUR = "#CCCEBE"

def get_quote():

    while True:
        quote_request = requests.get("https://zenquotes.io/api/random")
        quote_request.raise_for_status()
        quote_data = quote_request.json()
        print(quote_data)
        quote_line = quote_data[0]["q"]
        quote_by = quote_data[0]["a"]

        if len(quote_line) <= 100:
            canvas.itemconfig(quote, text=f"{quote_line}\n\n- {quote_by}")
            break

window = Tk()
window.title("Zen Quote of the Day")
window.config(padx=20, pady=20,bg=BACKGROUND_COLOUR)

bg_img = Image.open("images/bg1.png")
bg_img = bg_img.resize((800,600))
bg_img = ImageTk.PhotoImage(bg_img)

click_img = PhotoImage(file="images/click.png")
button_img = click_img.subsample(5, 5)

canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOUR, highlightthickness=0)
canvas.create_image(400,300,image=bg_img)
canvas.grid(row=0, column=0)

quote = canvas.create_text(400, 300, text=f"Quote of the day!",
                           font=("Gabriola", 15, "bold"), fill="#223E2B")

button = Button()
button.config(image=button_img, bg=BACKGROUND_COLOUR, command=get_quote)
button.grid(row=1, column=0)

window.mainloop()
