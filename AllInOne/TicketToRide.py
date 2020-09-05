import tkinter as tk
from tkinter import font as tkFont

############################################################

cost_of_station = 4
number_of_stations = 3
# Red, Yellow, Blue, Green, Black
header_colors = ["#c23616", "#e1b12c", "#192a56", "#44bd32", "#2f3640"]
score_colors = ["#e84118", "#fbc531", "#273c75", "#4cd137", "#353b48"]
text_colors = ["Black", "Black", "Black", "Black", "Black"]
############################################################

class TicketToRide:
    def __init__(self, scores):
        self.background_color = "Black"
        self.table_color = "#222222"
        self.text_color = "White"
        self.list_of_players = []
        self.scores = tk.Tk()
        self.root = tk.Tk()
        self.root.title("Controller")
        self.scores.title("Scores")
        self.buttons = []
        self.add_names()
        self.start_game()

    def get_players(self):
        for i, box in enumerate(self.textboxes):
            if (name := box.get()) != "":
                self.list_of_players.append(Player(name, i))

    def add_names(self):
        name_1 = tk.Entry(self.root)
        name_2 = tk.Entry(self.root)
        name_3 = tk.Entry(self.root)
        name_4 = tk.Entry(self.root)
        name_5 = tk.Entry(self.root)
        tk.Label(self.root, text="Player 1", fg = text_colors[0], bg = header_colors[0]).grid(row = 0, column = 0)
        tk.Label(self.root, text="Player 2", fg = text_colors[1], bg = header_colors[1]).grid(row = 1, column = 0)
        tk.Label(self.root, text="Player 3", fg = text_colors[2], bg = header_colors[2]).grid(row = 2, column = 0)
        tk.Label(self.root, text="Player 4", fg = text_colors[3], bg = header_colors[3]).grid(row = 3, column = 0)
        tk.Label(self.root, text="Player 5", fg = text_colors[4], bg = header_colors[4]).grid(row = 4, column = 0)
        start_button = tk.Button(self.root, text = "Start!", command = self.start_game)
        name_1.grid(row = 0, column = 1)
        name_2.grid(row = 1, column = 1)
        name_3.grid(row = 2, column = 1)
        name_4.grid(row = 3, column = 1)
        name_5.grid(row = 4, column = 1)
        start_button.grid(row = 5, column = 0, columnspan = 2, sticky="wesn")
        self.textboxes = [name_1, name_2, name_3, name_4, name_5]
        
        self.root.mainloop()
    
    def set_points_buttons(self):
        self.buttons = []
        for i in range(5):
            self.buttons.append(tk.Button(self.root, text = "1", command = lambda i=i: self.add_train(self.list_of_players[i], 1)))
            self.buttons.append(tk.Button(self.root, text = "2", command = lambda i=i: self.add_train(self.list_of_players[i], 2)))
            self.buttons.append(tk.Button(self.root, text = "3", command = lambda i=i: self.add_train(self.list_of_players[i], 3)))
            self.buttons.append(tk.Button(self.root, text = "4", command = lambda i=i: self.add_train(self.list_of_players[i], 4)))
            self.buttons.append(tk.Button(self.root, text = "6", command = lambda i=i: self.add_train(self.list_of_players[i], 6)))
            self.buttons.append(tk.Button(self.root, text = "8", command = lambda i=i: self.add_train(self.list_of_players[i], 8)))
            self.buttons.append(tk.Button(self.root, text = "🏠", command = lambda i=i: self.add_train(self.list_of_players[i], "station")))
            self.buttons.append(tk.Button(self.root, text = "-1", command = lambda i=i: self.add_train(self.list_of_players[i], -1)))

    def clear(self, window):
        for widget in window.winfo_children():
            widget.grid_forget()

    def start_game(self):
        self.get_players()
        self.clear(self.root)
        self.draw_scores()
        self.draw_buttons()
        self.root.mainloop()

    def draw_buttons(self):
        self.set_points_buttons()
        end_button = tk.Button(self.root, text = "End", command = self.longest_railroad)
        for i in range(len(self.list_of_players)):
            self.root.grid_columnconfigure(i, weight=1)
            for j in range(8):
                self.buttons[8*i+j].grid(row = j+2, column = i, sticky="wesn")
        end_button.grid(row = 10, column = 0, columnspan = len(self.list_of_players), sticky="nesw")
   
    def add_train(self, player, train):
        railroad_points = {
        1: 1,
        2: 2,
        3: 4,
        4: 7,
        6: 15,
        8: 21,
        -1: -1,
        }
        if train == "station" and player.stations_left > 0:
            player.stations_left -= 1
            player.add_points(-cost_of_station)
        else:
            player.add_points(railroad_points.get(train))
        self.draw_scores()
    
    def longest_railroad(self):
        self.clear(self.root)
        tk.Label(self.root, text="Pikim raudtee").grid(row=0, column=0, columnspan=len(self.list_of_players))
        for i, player in enumerate(self.list_of_players):
            tk.Button(self.root, text=player.name, fg = text_colors[player.color], bg = header_colors[player.color], command = lambda i=i: self.grande_finale(i)).grid(row=1, column=i)
        self.root.mainloop()

    def grande_finale(self, player_who_Got_10):
        self.list_of_players[player_who_Got_10].add_points(10)
        self.draw_scores()
        input_boxes = []
        finish = tk.Button(self.root, text="Done", command = lambda: self.finish_it_off(input_boxes))
        for i, player in enumerate(self.list_of_players):
            button = tk.Entry(self.root)
            input_boxes.append(button)
            button.grid(row=1, column=i)
        finish.grid(row=2, column=0, columnspan=len(self.list_of_players))
    
    def finish_it_off(self, input_boxes):
        for i, box in enumerate(input_boxes):
            self.list_of_players[i].add_points(int(box.get()))
        self.clear(self.root)
        self.draw_scores()

    def draw_score_window(self):
        self.scores.grid_rowconfigure(0, weight=1)
        self.scores.grid_rowconfigure(1, weight=3)
        border_width = 2
        font_family = "Helvetica"
        regular_font = tkFont.Font(family = font_family, size=72, weight = tkFont.BOLD)
        score_font = tkFont.Font(family = font_family, size=148)
        
        for i, player in enumerate(self.list_of_players):
            name = player.name
            score = str(player.score)
            border_relief = "raised"
            tk.Label(self.scores, text = name, borderwidth = border_width, relief = border_relief, font = regular_font, bg = header_colors[player.color], fg = text_colors[player.color]).grid(row = 0, column = i, sticky="wesn")
            tk.Label(self.scores, text = score, borderwidth = border_width, relief = border_relief, font = score_font, bg = score_colors[player.color], fg = text_colors[player.color]).grid(row = 1, column = i, sticky="wesn")
    
    def draw_scores(self):
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        border_width = 1
        height = 5
        width = 5
        font_family = "Helvetica"
        regular_font = tkFont.Font(family = font_family, size=48)
        
        for i, player in enumerate(self.list_of_players):
            name = player.name
            score = str(player.score)
            border_relief = "raised"
            self.scores.grid_columnconfigure(i, weight=1)
            tk.Label(self.root, text = name, borderwidth = 5, bg = header_colors[player.color], fg = text_colors[player.color], font = regular_font).grid(row = 0, column = i, sticky="wesn")
            tk.Label(self.root, text = score, font = regular_font).grid(row = 1, column = i, sticky="wesn")
        self.draw_score_window()

############################################################
class Player:
    def __init__(self, name, i):
        self.name = name.title()
        self.score = cost_of_station * number_of_stations
        self.stations_left = number_of_stations
        self.color = i
    
    def add_points(self, score):
        self.score += score

    def __repr__(self):
	    return self.name
        
############################################################

def main():
    game = TicketToRide()

if __name__ == '__main__':
    main()