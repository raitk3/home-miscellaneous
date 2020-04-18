import tkinter as tk
############################################################
cost_of_station = 4
number_of_stations = 3

class Player:
	def __init__(self, name):
		self.name = name.capitalize()
		self.score = cost_of_station * number_of_stations
		self.stations_left = number_of_stations

	def add_points(self, score):
		self.score += score

	def __repr__(self):
		return self.name
        
############################################################

def get_players():
    for box in textboxes:
        if (name := box.get()) != "":
            list_of_players.append(Player(name))

def remove_names():
    get_players()
    for widget in root.winfo_children():
        widget.grid_forget()
    print(list_of_players)
    draw_scores()
    draw_buttons()
    root.mainloop()

    
def add_names():
    tk.Label(root, text="Player 1").grid(row = 0, column = 0)
    tk.Label(root, text="Player 2").grid(row = 1, column = 0)
    tk.Label(root, text="Player 3").grid(row = 2, column = 0)
    tk.Label(root, text="Player 4").grid(row = 3, column = 0)
    tk.Label(root, text="Player 5").grid(row = 4, column = 0)
    name_1.grid(row = 0, column = 1)
    name_2.grid(row = 1, column = 1)
    name_3.grid(row = 2, column = 1)
    name_4.grid(row = 3, column = 1)
    name_5.grid(row = 4, column = 1)
    start_button.grid(row = 5, column = 0)
    root.mainloop()

def draw_scores():
    for i, player in enumerate(list_of_players):
        name = player.name
        score = str(player.score)
        tk.Label(root, text = name, borderwidth = 5, bg = 'green').grid(row = 0, column = i)
        tk.Label(root, text = score).grid(row = 1, column = i)

def draw_buttons():
    set_points_buttons()
    for i in range(len(list_of_players)):
        for j in range(6):
            buttons[i+j*5].grid(row = j+2, column = i)


def add_train(player, train):
    print(len(list_of_players))
    railroad_points = {
    0: 0,
    1: 1,
    2: 2,
    3: 4,
    4: 7,
    6: 15,
    8: 21,
    }
    player.add_points(railroad_points.get(train))
    draw_scores()

def set_points_buttons():
    for i in range(5):
        buttons[i] = tk.Button(root, text = "1", command = lambda i=i: add_train(list_of_players[i], 1))
        buttons[i+5] = tk.Button(root, text = "2", command = lambda i=i: add_train(list_of_players[i], 2))
        buttons[i+10] = tk.Button(root, text = "3", command = lambda i=i: add_train(list_of_players[i], 3))
        buttons[i+15] = tk.Button(root, text = "4", command = lambda i=i: add_train(list_of_players[i], 4))
        buttons[i+20] = tk.Button(root, text = "6", command = lambda i=i: add_train(list_of_players[i], 6))
        buttons[i+25] = tk.Button(root, text = "8", command = lambda i=i: add_train(list_of_players[i], 8))

#PLAYERS####################################################

list_of_players = []

root = tk.Tk()

name_1 = tk.Entry(root)
name_2 = tk.Entry(root)
name_3 = tk.Entry(root)
name_4 = tk.Entry(root)
name_5 = tk.Entry(root)
textboxes = [name_1, name_2, name_3, name_4, name_5]


#BUTTONS####################################################

buttons = [tk.Button() for _ in range(6*5)]

start_button = tk.Button(root, text = "Start!", command = remove_names)



add_names()