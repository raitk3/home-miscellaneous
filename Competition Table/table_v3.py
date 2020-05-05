import tkinter as tk
import os.path
from tkinter import font as tkFont
from pathlib import Path
#Windows
class Input:
    def __init__(self, tournament):
        super().__init__()
        self.tournament = tournament
        self.window = tk.Tk()
        self.window.title("Input")
    
    def ask_number_of_players(self):
        tk.Label(self.window, text="Tiimide arv").grid(row=0,column=0,columnspan=2)
        number_of_players = tk.Entry(self.window)
        ask_button = tk.Button(self.window, text="OK", command = lambda: self.ask_team_names(int(number_of_players.get())))
        number_of_players.grid(row=1,column=0)
        ask_button.grid(row=1,column=1)
        self.window.mainloop()

    def ask_team_names(self, number_of_players):
        self.clear_window()
        text_boxes = []
        tk.Label(self.window, text="Tiimide nimed").grid(row=0,column=0,columnspan=2)
        i = 1
        while i <= number_of_players:
            tk.Label(self.window, text=f"Tiim {i}").grid(row=i, column=0)
            text_box = tk.Entry(self.window)
            text_box.grid(row=i, column=1)
            text_boxes.append(text_box)
            i += 1
        start_button = tk.Button(self.window, text="Start!", command = lambda: self.tournament.start([text_box.get() for text_box in text_boxes])).grid(row=i, column=0,columnspan=2)
        self.window.mainloop()

    def show_games(self):
        self.clear_window()
    
    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.grid_forget()

class Games:
    def __init__(self, tournament):
        super().__init__()
        self.tournament = tournament
        self.window = self.tournament.input.window
        self.window.title("Games")
        self.games = {}

    def show_games(self):
        number_of_rows = 18
        self.clear_window()
        for i, game in enumerate(self.games):
            tk.Button(self.window, text=f"{game[0]} vs {game[1]}", command=lambda game=game: self.get_result(game)).grid(row=i % number_of_rows, column=(i // number_of_rows)*2, sticky="esnw")
            result = tk.Label(self.window, text=f"{self.games[game][0]}:{self.games[game][1]}")
            if self.games[game] == "N/A":
                result = tk.Label(self.window, text="N/A")
            result.grid(row=i % number_of_rows, column=(i // number_of_rows) * 2 + 1)
        if self.get_end():
            tk.Button(self.window, text = "Finish").grid(row = min(number_of_rows, len(self.games)) + 1, column = 0, columnspan = (len(self.games) // number_of_rows)*2 + 2, sticky="nesw")
    
    def get_end(self):
        for team in self.tournament.teams:
            if team.get_games() != len(self.tournament.teams) - 1:
                return False
        return True

    def get_games(self):
        for i in range(len(self.tournament.teams)):
            for j in range(i+1, len(self.tournament.teams)):
                self.games[(self.tournament.teams[i], self.tournament.teams[j])] = "N/A"   

    def get_result(self, playing_teams):
        self.clear_window()
        tk.Label(self.window, text=str(playing_teams[0])).grid(row=0, column=0)
        team_1_score = tk.Entry(self.window)
        team_1_score.grid(row=0, column=1)
        tk.Label(self.window, text=":").grid(row=0, column=2)
        team_2_score = tk.Entry(self.window)
        team_2_score.grid(row=0, column=3)
        tk.Label(self.window, text=str(playing_teams[1])).grid(row=0, column=4)
        tk.Button(self.window, text="Set result", command=lambda: self.set_result(playing_teams, (int(team_1_score.get()), int(team_2_score.get())))).grid(row=1, column=0, columnspan=3, sticky="esnw")
        tk.Button(self.window, text="Clear result", command=lambda: self.clear_result(playing_teams)).grid(row=1, column=3, columnspan=2, sticky="esnw")
    
    def set_result(self, playing_teams: tuple, result: tuple):
        self.games[playing_teams] = result
        self.tournament.loop()

    def clear_result(self, playing_teams: tuple):
        self.games[playing_teams] = "N/A"
        self.tournament.loop()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.grid_forget()

class Table:
    def __init__(self, tournament):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("Scoresheet")
        self.tournament = tournament

    def update(self):
        border_width = 2
        bold_relief = "groove"
        regular_relief_1 = "sunken"
        points_relief = "sunken"
        font_family = "Helvetica"
        header_font = tkFont.Font(self.window, family = font_family, size=18)
        regular_font = tkFont.Font(self.window, family = font_family, size=48)
        bold_font = tkFont.Font(self.window, family = font_family, size=24, weight = tkFont.BOLD)

        tk.Label(self.window, borderwidth = border_width, relief = bold_relief, text="Tiim", font = header_font).grid(row = 0, column = 0, sticky='EWNS')
        tk.Label(self.window, borderwidth = border_width, relief = bold_relief, text="Mängud", font = header_font).grid(row = 0, column = 1, sticky='EWNS')
        tk.Label(self.window, borderwidth = border_width, relief = bold_relief, text="Võidud", font = header_font).grid(row = 0, column = 2, sticky='EWNS')
        #tk.Label(self.window, borderwidth = border_width, relief = bold_relief, text="Viigid", font = header_font).grid(row = 0, column = 3, sticky='EWNS')
        tk.Label(self.window, borderwidth = border_width, relief = bold_relief, text="Kaotused", font = header_font).grid(row = 0, column = 3, sticky='EWNS')
        tk.Label(self.window, borderwidth = border_width, relief = bold_relief, text="Võidetud\nlahingud", font = header_font).grid(row = 0, column = 4, sticky='EWNS')
        tk.Label(self.window, borderwidth = border_width, relief = bold_relief, text="Kaotatud\nlahingud", font = header_font).grid(row = 0, column = 5, sticky='EWNS')
        tk.Label(self.window, borderwidth = border_width, relief = bold_relief, text="Lahingute\nvahe", font = header_font).grid(row = 0, column = 6, sticky='EWNS')
        tk.Label(self.window, borderwidth = border_width, relief = bold_relief, text="Punktid", font = header_font).grid(row = 0, column = 7, sticky='EWNS')

        sorted_table = sorted(self.tournament.teams, key=lambda x: [x.get_score(), x.rounds_won], reverse = True)
        for i in range(1, 8):
            tk.Grid.columnconfigure(self.window, i, weight=1)
        for i, team in enumerate(sorted_table):
            tk.Grid.rowconfigure(self.window, i+1, weight=1)
            tk.Label(self.window, borderwidth = border_width, relief = bold_relief,  text=team.name, font = bold_font, anchor = "w").grid(row = i+1, column = 0, sticky='EWNS')
            tk.Label(self.window, borderwidth = border_width, relief = regular_relief_1, text=str(team.get_games()), font = regular_font).grid(row = i+1, column = 1, sticky='EWNS')
            tk.Label(self.window, borderwidth = border_width, relief = regular_relief_1, text=str(team.wins), font = regular_font).grid(row = i+1, column = 2, sticky='EWNS')
            #tk.Label(self.window, borderwidth = border_width, relief = regular_relief_1, text=str(team.draws), font = regular_font).grid(row = i+1, column = 3, sticky='EWNS')
            tk.Label(self.window, borderwidth = border_width, relief = regular_relief_1, text=str(team.defeats), font = regular_font).grid(row = i+1, column = 3, sticky='EWNS')
            tk.Label(self.window, borderwidth = border_width, relief = regular_relief_1, text=str(team.rounds_won), font = regular_font).grid(row = i+1, column = 4, sticky='EWNS')
            tk.Label(self.window, borderwidth = border_width, relief = regular_relief_1, text=str(team.rounds_lost), font = regular_font).grid(row = i+1, column = 5, sticky='EWNS')
            tk.Label(self.window, borderwidth = border_width, relief = regular_relief_1, text=str(team.get_round_diff()), font = regular_font).grid(row = i+1, column = 6, sticky='EWNS')
            tk.Label(self.window, borderwidth = border_width, relief = points_relief, text=str(team.get_score()), font = regular_font).grid(row = i+1, column = 7, sticky='EWNS')

#Team
class Team:

    def __init__(self, name, tournament):
        super().__init__()
        self.tournament = tournament
        self.wins = 0
        self.draws = 0
        self.defeats = 0
        self.rounds_won = 0
        self.rounds_lost = 0
        self.name = name

    def get_personal_games(self):
        team_games = {}
        for game in self.tournament.games.games:
            if self in game:
                team_games[game] = self.tournament.games.games[game]
        return team_games

    def get_current_status(self):
        self.wins = 0
        self.draws = 0
        self.defeats = 0
        self.rounds_won = 0
        self.rounds_lost = 0
        for game in self.get_personal_games():
            if self.tournament.games.games[game] != "N/A":
                me = game[0]
                opponent = game[1]
                my_score = self.tournament.games.games[game][0]
                opponent_score = int(self.tournament.games.games[game][1])
                if self is not me:
                    me = game[1]
                    opponent = game[0]
                    my_score = self.tournament.games.games[game][1]
                    opponent_score = self.tournament.games.games[game][0]
                
                if my_score > opponent_score:
                    self.wins += 1
                elif my_score == opponent_score:
                    self.draws += 1
                else:
                    self.defeats += 1
                self.rounds_won += my_score
                self.rounds_lost += opponent_score

    def get_games(self):
        return self.wins + self.draws + self.defeats     
    
    def get_score(self):
        return self.wins * self.tournament.win_points + self.draws * self.tournament.draw_points + self.defeats * self.tournament.loss_points
    
    def get_round_diff(self):
        return self.rounds_won - self.rounds_lost

    def __repr__(self):
        return self.name

#Tournament 
class Tournament:
    
    def __init__(self, win, draw, loss):
        super().__init__()
        self.teams=[]
        self.win_points = win
        self.draw_points = draw
        self.loss_points = loss
        self.input = Input(self)
        self.table = None
        self.games = None
        self.get_teams("teams.txt")

    def get_teams(self, filename):
        myFile = Path(filename)
        team_names = []
        if myFile.is_file():
            with open(filename, encoding="utf8") as file:
                for line in file.readlines():
                    team_names.append(line.strip())
            self.start(team_names)
        else:
            self.input.ask_number_of_players()

    def start(self, names):
        self.table = Table(self)
        self.games = Games(self)
        for name in names:
            team = Team(name, self)
            self.teams.append(team)
        print(self.teams)
        self.games.get_games()
        self.loop()
        self.input.window.mainloop()
    
    def update_teams(self):
        for team in self.teams:
            team.get_current_status()

    def loop(self):
        self.update_teams()
        self.table.update()
        self.games.show_games()
    
if __name__ == "__main__":
    tournament = Tournament(1, 0, 0)
