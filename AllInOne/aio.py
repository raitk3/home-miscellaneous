import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk
from games import scrabble, ticket_to_ride

def begin(game, root):
    if game == "Ticket to Ride":
        root.destroy()
        ticket_to_ride.main()
    elif game == "Scrabble":
        root.destroy()
        scrabble.main()
    else:
        print("Wth?")

def draw_picker(root):
    games_list = ["Scrabble", "Ticket to Ride"]
    game = ttk.Combobox(root, values=games_list)
    button = tk.Button(root, text="Start!", command=lambda: begin(game.get(), root))
    game.grid(row = 0, column = 0)
    button.grid(row = 1, column = 0)


if __name__ == '__main__':
    root = tk.Tk()
    draw_picker(root)
    root.mainloop()
