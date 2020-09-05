import tkinter as tk
from tkinter import ttk
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

    def get_result(self, playing_teams):
        self.window = tk.Tk()
        self.window.title("Result")
        tk.Label(self.window, text=str(playing_teams[0])).grid(row=0, column=0)
        team_1_score = tk.Entry(self.window)
        team_1_score.grid(row=0, column=1)
        tk.Label(self.window, text=":").grid(row=0, column=2)
        team_2_score = tk.Entry(self.window)
        team_2_score.grid(row=0, column=3)
        tk.Label(self.window, text=str(playing_teams[1])).grid(row=0, column=4)
        ttk.Button(self.window, text="Set result", command=lambda: self.tournament.games.set_result(playing_teams, (int(team_1_score.get()), int(team_2_score.get())))).grid(row=1, column=0, columnspan=3, sticky="esnw")
        ttk.Button(self.window, text="Clear result", command=lambda: self.tournament.games.clear_result(playing_teams)).grid(row=1, column=3, columnspan=2, sticky="esnw")
  
    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.grid_forget()

class Games:
    def __init__(self, tournament):
        super().__init__()
        self.tournament = tournament
        self.window = tk.Tk()
        self.window.title("Games")
        self.games_order=[]  #Robocode specific
        self.games = {}

    def show_games(self):
        number_of_games = len(self.games)
        max_columns = 6
        number_of_rows = 0
        for i in range(2, max_columns):
            if number_of_rows == 0:
                temp_rows = number_of_games // i
                if number_of_games % i == 0 and temp_rows < 20:
                    number_of_rows = temp_rows
        
        self.clear_window()
        for i, game in enumerate(self.games):
            ttk.Button(self.window, text=f"{game[0]} vs {game[1]}", command=lambda game=game: self.tournament.input.get_result(game)).grid(row=i % number_of_rows, column=(i // number_of_rows)*2, sticky="esnw")
            result = ttk.Label(self.window, text=f"{self.games[game][0]}:{self.games[game][1]}")
            if self.games[game] == "N/A":
                result = tk.Label(self.window, text="N/A")
            result.grid(row=i % number_of_rows, column=(i // number_of_rows) * 2 + 1)
        if self.get_end():
            tk.ttk.Button(self.window, text = "Finish", command = self.tournament.end).grid(row = min(number_of_rows, len(self.games)) + 1, column = 0, columnspan = (len(self.games) // number_of_rows)*2 + 2, sticky="nesw")

    def get_end(self):
        for game in self.games:
            if self.games[game] == "N/A":
                return False
        return True

    def get_games(self):
        for i in range(len(self.tournament.teams)):
            for j in range(i+1, len(self.tournament.teams)):
                self.games[(self.tournament.teams[i], self.tournament.teams[j])] = "N/A"   

    def set_result(self, playing_teams: tuple, result: tuple):
        self.games[playing_teams] = result
        self.tournament.loop()

    def clear_result(self, playing_teams: tuple):
        self.games[playing_teams] = "N/A"
        self.tournament.loop()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.grid_forget()

    def get_writable_games(self):
        return [f"{game[0]} {self.games[game][0]}:{self.games[game][1]} {game[1]}" for game in self.games]

class Table:
    def __init__(self, tournament):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("Scoresheet")
        self.tournament = tournament
        self.style = ttk.Style()

        border_width = 10
        bold_relief = "solid"
        regular_relief_1 = "solid"
        points_relief = "solid"
        header_font = ("Coluna Rounded", 28)
        regular_font = ("Coluna Rounded", 36)
        bold_font = ("Coluna Rounded", 24)
        
        self.style = ttk.Style(self.window)
        self.style.configure("Header.TLabel", background = "#232652", foreground="white", borderwidth=2, relief=bold_relief, font=header_font, anchor=tk.CENTER, justify=tk.CENTER, weight="bold", padding=5)
        self.style.configure("Teams.TLabel", background = "#232652", foreground="white", borderwidth=border_width, relief=regular_relief_1, font=bold_font, anchor=tk.W, justify=tk.CENTER, wraplength=400, padding=5)
        self.style.configure("Table.TLabel", background = "#232652", foreground="white", borderwidth=1, relief=regular_relief_1, font=regular_font, anchor=tk.CENTER, justify=tk.CENTER, padding=5)
        self.style.configure("Points.TLabel", background = "#232652", foreground="white", borderwidth=1, relief=regular_relief_1, font=regular_font, anchor=tk.CENTER, justify=tk.CENTER, padding=5)
    

    def update(self):
        headers = ["Name", "M", "W", "D", "L", "GS", "GC", "GD", "P"]
        for i, header in enumerate(headers):
            ttk.Label(self.window, style = "Header.TLabel", text=header).grid(row = 0, column = i, sticky='EWNS')    

        sorted_table = sorted(self.tournament.teams, key=lambda x: (x.get_score(), x.get_round_diff(), x.rounds_won), reverse = True)
        for i in range(1, len(headers)):
            tk.Grid.columnconfigure(self.window, i, weight=1)
        for i, team in enumerate(sorted_table):
            tk.Grid.rowconfigure(self.window, i+1, weight=1)
            data = [team.name, team.get_games(), team.wins, team.draws, team.defeats, team.rounds_won, team.rounds_lost, team.get_round_diff(), team.get_score()]
            for j, data_label in enumerate(data):
                if j == 0:
                    ttk.Label(self.window, style="Teams.TLabel", text=data_label, anchor = "w").grid(row = i+1, column = j, sticky='EWNS')
                elif data_label == data[-1]:
                    ttk.Label(self.window, style="Points.TLabel", text=str(data_label)).grid(row = i+1, column = j, sticky='EWNS')
                else:
                    ttk.Label(self.window, style="Table.TLabel", text=str(data_label)).grid(row = i+1, column = j, sticky='EWNS')
                
    def get_table(self):
        list_of_writable_lines = []
        sorted_table = sorted(self.tournament.teams, key=lambda x: [x.get_score(), x.get_round_diff()], reverse = True)
        longest_name = max(max([len(name) for name in [el for el in [team.name for team in self.tournament.teams]]]), 4)
        
        writable_separator = f"+{'':->{longest_name+2}}+{'':->3}+{'':->4}+{'':->4}+{'':->4}+{'':->4}+{'':->4}+{'':->5}+{'':->4}+"
        
        list_of_writable_lines.append(writable_separator)
        list_of_writable_lines.append(f"| {'Nimi': >{longest_name}} | {'M':>1} | {'Võ':>2} | {'Vi':>2} | {'K':>2} | {'VL':>2} | {'KL':>2} | {'LV':>3} | {'P':>2} |")
        
        for i, team in enumerate(sorted_table):
            list_of_writable_lines.append(writable_separator)
            list_of_writable_lines.append(f"| {team.name: >{longest_name}} | {team.get_games():>1} | {team.wins:>2} | {team.draws:>2} | {team.defeats:>2} | {team.rounds_won:>2} | {team.rounds_lost:>2} | {team.get_round_diff():>3} | {team.get_score():>2} |")
        list_of_writable_lines.append(writable_separator)
        
        return list_of_writable_lines

class Table_Mini:
    def __init__(self, tournament):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("Scoresheet Mini")
        self.tournament = tournament
        self.style = ttk.Style()

        border_width = 0
        bold_relief = "solid"
        regular_relief_1 = "solid"
        points_relief = "solid"
        header_font = ("Coluna Rounded", 28)
        regular_font = ("Coluna Rounded", 36)
        bold_font = ("Coluna Rounded", 24)
        
        self.style = ttk.Style(self.window)
        self.style.configure("Header.TLabel", background = "#232652", foreground="white", borderwidth=border_width, relief=bold_relief, highlightcolor="pink", font=header_font, anchor=tk.CENTER, justify=tk.CENTER, weight="bold", padding=5)
        self.style.configure("Teams.TLabel", background = "#232652", foreground="white", borderwidth=border_width, relief=regular_relief_1, font=bold_font, anchor=tk.W, justify=tk.CENTER, wraplength=400, padding=5)
        self.style.configure("Points.TLabel", background = "#232652", foreground="white", borderwidth=border_width, relief=regular_relief_1, font=regular_font, anchor=tk.CENTER, justify=tk.CENTER, padding=5)
    

    def update(self):
        
        ttk.Label(self.window, style = "Header.TLabel", text="Leaderboard").grid(row = 0, column = 0, columnspan=2, sticky='EWNS')

        sorted_table = sorted(self.tournament.teams, key=lambda x: (x.get_score(), x.get_round_diff(), x.rounds_won), reverse = True)
        tk.Grid.columnconfigure(self.window, 0, weight=3)
        tk.Grid.columnconfigure(self.window, 1, weight=1)
        for i, team in enumerate(sorted_table):
            tk.Grid.rowconfigure(self.window, i+1, weight=1)
            ttk.Label(self.window, style="Teams.TLabel", text=team.name, anchor = "w").grid(row = i+1, column = 0, sticky='EWNS')
            ttk.Label(self.window, style="Points.TLabel", text=str(team.get_score())).grid(row = i+1, column = 1, sticky='EWNS')


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
        self.table_mini = None
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
        #self.table_mini = Table_Mini(self)
        self.games = Games(self)
        for name in names:
            team = Team(name, self)
            self.teams.append(team)
        self.games.get_games()
        self.loop()
        self.input.window.mainloop()
    
    def update_teams(self):
        for team in self.teams:
            team.get_current_status()

    def end(self):
        with open("results.txt", "w") as file:
            file.writelines("\n".join(self.table.get_table()))
            file.write("\n")
            file.writelines("\n".join(self.games.get_writable_games()))
    
    def loop(self):
        self.input.window.destroy()
        self.update_teams()
        self.table.update() #Comment this if you don't want the big one
        #self.table_mini.update()
        self.games.show_games()
 

if __name__ == "__main__":
    tournament = Tournament(3, 1, 0)
