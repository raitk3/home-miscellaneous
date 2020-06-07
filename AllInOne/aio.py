import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk
import TicketToRide
import scrabble

def begin(game, root):
    if game == "Ticket to Ride":
        root.destroy()
        TicketToRide.main()
    elif game == "Scrabble":
        root.destroy()
        scrabble.main()
    else:
        print("Wth?")

if __name__ == '__main__':
    root = tk.Tk()
    games_list = ["Scrabble", "Ticket to Ride"]
    game = ttk.Combobox(root, values=games_list)
    button = tk.Button(root, text="Start!", command=lambda: begin(game.get(), root))
    game.grid(row = 0, column = 0)
    button.grid(row = 1, column = 0)
    root.mainloop()
