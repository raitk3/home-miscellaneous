import os
import tkinter as tk
import math
import random
import time

class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Scoreboard:
    def __init__(self):
        root = tk.Tk()
        root.title("Scoreboard")
        tk.Label(root, text = "What the fuck am I?").pack()

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Controller")
        tk.Label(self.root, text="Siia tulevad nupud, juhheii!").pack()
        self.root.mainloop()

class Game:
    def __init__(self):
        self.root = tk.Tk()

if __name__ == '__main__':
    scoreboard = Scoreboard()
    controller = Controller()
    