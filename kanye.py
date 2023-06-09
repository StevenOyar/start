import requests
from tkinter import *


def get_quote():
    
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)

quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 24, "bold")
                                , fill="blue")
canvas.grid(row=0, column=0)


kanye_button = Button(highlightthickness=0, command=get_quote, text="Kanye Once said", fg="brown", bg="teal")
kanye_button.grid(row=1, column=0, columnspan=2)


window.mainloop()