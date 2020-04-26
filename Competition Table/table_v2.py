import tkinter as tk
from tkinter import font as tkFont

class Team:
    name = ""
    wins = 0
    draws = 0
    defeats = 0
    rounds_won = 0
    rounds_lost = 0

    def __init__(self, name):
        super().__init__()
        self.name = name

    def add_rounds(self, rounds_won, rounds_lost):
        self.rounds_won += rounds_won
        self.rounds_lost += rounds_lost

    def win(self, rounds_won, rounds_lost):
        self.wins += 1
        self.add_rounds(rounds_won, rounds_lost)

    def draw(self, rounds_won, rounds_lost):
        self.draws += 1
        self.add_rounds(rounds_won, rounds_lost)
        
    def defeat(self, rounds_won, rounds_lost):
        self.defeats += 1
        self.add_rounds(rounds_won, rounds_lost)
    
    def get_games(self):
        return self.wins + self.draws + self.defeats     
    
    def get_score(self):
        return self.wins * 3 + self.draws
    
    def get_round_diff(self):
        return self.rounds_won - self.rounds_lost

    def __repr__(self):
        return f"{self.name}: {self.get_score()} points"

class Table:
    teams = []
    team_names = {}
    games = {}
    third_place_game = ""
    first_place_game = ""
    third = Team("")
    second = Team("")
    first = Team("")

    def __init__(self):
        number_of_teams = int(input("Number of teams: "))
        i = 0
        while i in range(number_of_teams):
            if (name := input(f"Team {i+1}: ")) in self.team_names:
                continue
            self.teams.append(Team(name))
            self.team_names[name] = i
            i += 1
    
    def get_team_and_score(self, input_string):
        team_name, team_score = input_string.split("-")
        return team_name.strip(), int(team_score.strip())
    
    def parse_input(self, input_string):
        if input_string == "games":
            self.print_games()
            return True
        try:
            team_1, team_2 = input_string.split(",")

            team_1_name, team_1_score = self.get_team_and_score(team_1)
            team_2_name, team_2_score = self.get_team_and_score(team_2)
            if f"{team_1_name} - {team_2_name}" not in self.games and team_1_name != team_2_name:
                winner_name = team_1_name if team_1_score > team_2_score else team_2_name
                loser_name = team_1_name if winner_name == team_2_name else team_2_name
                winner_score = max(team_1_score, team_2_score)
                loser_score = min(team_1_score, team_2_score)

                winner = self.teams[self.team_names[winner_name]]
                loser = self.teams[self.team_names[loser_name]]

                if team_1_score == team_2_score:
                    winner.draw(winner_score, loser_score)
                    loser.draw(loser_score, winner_score)
                else:
                    winner.win(winner_score, loser_score)
                    loser.defeat(loser_score, winner_score)
                self.games[f"{team_1_name} - {team_2_name}"] = f"{team_1_score}:{team_2_score}"
                return True
            print("Wrong input!")

        except:
            print("Wrong input!")

    def get_games(self):
        return [f"{game} {self.games[game]}" for game in self.games]

    def print_games(self):
        print(*self.get_games(), sep="\n")

    def get_table(self):
        list_of_writable_lines = []
        sorted_table = sorted(self.teams, key=lambda x: [x.get_score(), x.rounds_won], reverse = True)
        longest_name = max(max([len(name) for name in [el for el in self.team_names]]), 4)
        
        writable_separator = f"+{'':->{longest_name+2}}+{'':->3}+{'':->4}+{'':->4}+{'':->4}+{'':->4}+{'':->4}+{'':->5}+{'':->4}+"
        
        list_of_writable_lines.append(writable_separator)
        list_of_writable_lines.append(f"| {'Nimi': >{longest_name}} | {'M':>1} | {'Võ':>2} | {'Vi':>2} | {'K':>2} | {'VR':>2} | {'KR':>2} | {'RS':>3} | {'P':>2} |")
        
        for i, team in enumerate(sorted_table):
            list_of_writable_lines.append(writable_separator)
            list_of_writable_lines.append(f"| {team.name: >{longest_name}} | {team.get_games():>1} | {team.wins:>2} | {team.draws:>2} | {team.defeats:>2} | {team.rounds_won:>2} | {team.rounds_lost:>2} | {team.get_round_diff():>3} | {team.get_score():>2} |")
        list_of_writable_lines.append(writable_separator)
        
        return list_of_writable_lines

    def update_table_window(self, table_window):

        border_width = 2
        bold_relief = "raised"
        regular_relief_1 = "groove"
        regular_relief_2 = "groove"
        font_family = "Helvetica"
        regular_font = tkFont.Font(family = font_family, size=48)
        bold_font = tkFont.Font(family = font_family, size=48, weight = tkFont.BOLD)

        tk.Label(table_window, borderwidth = border_width, relief = bold_relief, text="Team", font = bold_font).grid(row = 0, column = 0, sticky='EWNS')
        tk.Label(table_window, borderwidth = border_width, relief = bold_relief, text="M", font = bold_font).grid(row = 0, column = 1, sticky='EWNS')
        tk.Label(table_window, borderwidth = border_width, relief = bold_relief, text="Võ", font = bold_font).grid(row = 0, column = 2, sticky='EWNS')
        tk.Label(table_window, borderwidth = border_width, relief = bold_relief, text="Vi", font = bold_font).grid(row = 0, column = 3, sticky='EWNS')
        tk.Label(table_window, borderwidth = border_width, relief = bold_relief, text="K", font = bold_font).grid(row = 0, column = 4, sticky='EWNS')
        tk.Label(table_window, borderwidth = border_width, relief = bold_relief, text="RV", font = bold_font).grid(row = 0, column = 5, sticky='EWNS')
        tk.Label(table_window, borderwidth = border_width, relief = bold_relief, text="RK", font = bold_font).grid(row = 0, column = 6, sticky='EWNS')
        tk.Label(table_window, borderwidth = border_width, relief = bold_relief, text="RV", font = bold_font).grid(row = 0, column = 7, sticky='EWNS')
        tk.Label(table_window, borderwidth = border_width, relief = bold_relief, text="P", font = bold_font).grid(row = 0, column = 8, sticky='EWNS')

        sorted_table = sorted(self.teams, key=lambda x: [x.get_score(), x.rounds_won], reverse = True)

        for i, team in enumerate(sorted_table):
            tk.Label(table_window, borderwidth = border_width, relief = bold_relief,  text=team.name, font = bold_font, anchor = "w").grid(row = i+1, column = 0, sticky='EWNS')
            tk.Label(table_window, borderwidth = border_width, relief = regular_relief_1, text=str(team.get_games()), font = regular_font).grid(row = i+1, column = 1, sticky='EWNS')
            tk.Label(table_window, borderwidth = border_width, relief = regular_relief_2, text=str(team.wins), font = regular_font).grid(row = i+1, column = 2, sticky='EWNS')
            tk.Label(table_window, borderwidth = border_width, relief = regular_relief_2, text=str(team.draws), font = regular_font).grid(row = i+1, column = 3, sticky='EWNS')
            tk.Label(table_window, borderwidth = border_width, relief = regular_relief_2, text=str(team.defeats), font = regular_font).grid(row = i+1, column = 4, sticky='EWNS')
            tk.Label(table_window, borderwidth = border_width, relief = regular_relief_1, text=str(team.rounds_won), font = regular_font).grid(row = i+1, column = 5, sticky='EWNS')
            tk.Label(table_window, borderwidth = border_width, relief = regular_relief_1, text=str(team.rounds_lost), font = regular_font).grid(row = i+1, column = 6, sticky='EWNS')
            tk.Label(table_window, borderwidth = border_width, relief = regular_relief_1, text=str(team.get_round_diff()), font = regular_font).grid(row = i+1, column = 7, sticky='EWNS')
            tk.Label(table_window, borderwidth = border_width, relief = regular_relief_2, text=str(team.get_score()), font = regular_font).grid(row = i+1, column = 8, sticky='EWNS')

    def update_games_window(self, games_window):
        font_family = "Helvetica"
        tk_font = tkFont.Font(family = font_family, size=48, weight = tkFont.BOLD)

        for i, game in enumerate(self.games):
            
            tk.Label(games_window, borderwidth = 2, relief = "ridge", font = tk_font, text=game).grid(row=i, column=0, sticky='EWNS')
            tk.Label(games_window, borderwidth = 2, relief = "ridge", font = tk_font, text=self.games[game]).grid(row=i, column=1, sticky='EWNS') 
    
    def update_windows(self,table_window, games_window):
        self.update_games_window(games_window)
        self.update_table_window(table_window)

    def get_third_place(self):
        input_string = input("Third place match result: ")
        try:
            team_1, team_2 = input_string.split(",")

            team_1_name, team_1_score = self.get_team_and_score(team_1)
            team_2_name, team_2_score = self.get_team_and_score(team_2)
            sorted_table = sorted(self.teams, key=lambda x: [x.get_score(), x.rounds_won], reverse = True)
            if team_1_name == sorted_table[2].name and team_2_name == sorted_table[3].name:
                winner_name = team_1_name if team_1_score > team_2_score else team_2_name
                loser_name = team_1_name if winner_name == team_2_name else team_2_name
                winner_score = max(team_1_score, team_2_score)
                loser_score = min(team_1_score, team_2_score)

                winner = self.teams[self.team_names[winner_name]]
                loser = self.teams[self.team_names[loser_name]]
                self.third_place_game = f"{team_1_name} {team_1_score}:{team_2_score} {team_2_name}"
                self.third = winner
                return True
            return False

        except:
            print("Wrong input!")
            return False
        
    def get_winner(self):
        input_string = input("First place match result: ")
        try:
            team_1, team_2 = input_string.split(",")

            team_1_name, team_1_score = self.get_team_and_score(team_1)
            team_2_name, team_2_score = self.get_team_and_score(team_2)
            sorted_table = sorted(self.teams, key=lambda x: [x.get_score(), x.rounds_won], reverse = True)
            if team_1_name == sorted_table[0].name and team_2_name == sorted_table[1].name:
                winner_name = team_1_name if team_1_score > team_2_score else team_2_name
                loser_name = team_1_name if winner_name == team_2_name else team_2_name
                winner_score = max(team_1_score, team_2_score)
                loser_score = min(team_1_score, team_2_score)

                winner = self.teams[self.team_names[winner_name]]
                loser = self.teams[self.team_names[loser_name]]
                self.first_place_game = f"{team_1_name} {team_1_score}:{team_2_score} {team_2_name}"
                self.second = loser
                self.first = winner
                return True
            return False
        except:
            print("Wrong input!")
            return False

    def get_end(self):
        for team in self.teams:
            if team.get_games() != 2 * (len(self.teams) - 1):
                return False
        return True

    def finish(self):
        with open("results.txt", "w") as file:
            file.writelines("\n".join(self.get_table()))
            file.write("\n")
            file.writelines("\n".join(self.get_games()))
            file.write("\nThird place match result: " + self.third_place_game)
            file.write("\nTop 3:\n")
            file.write("First place match result: " + self.first_place_game + "\n")
            file.write(self.first.name + "\n")
            file.write(self.second.name + "\n")
            file.write(self.third.name + "\n")
        print("Third place match result: " + self.third_place_game)
        print("First place match result: " + self.first_place_game)
        print("Top 3:")
        print(self.first.name)
        print(self.second.name)
        print(self.third.name)
    
            

if __name__ == "__main__":
    table = Table()
    table_window = tk.Tk()
    table_window.title("Table")
    games_window = tk.Tk()
    games_window.title("Games played")
    table.update_windows(table_window, games_window)
    while not table.get_end():
        input_string = input()
        table.parse_input(input_string)
        table.update_windows(table_window, games_window)

    if len(table.team_names) > 2:
        if len(table.team_names) > 3:
            while not table.get_third_place():
                continue
        else:
            table.third = sorted(table.teams, key=lambda x: [x.get_score(), x.rounds_won], reverse = True)[2]
            table.third_place_game = "N/A"
    if len(table.team_names) > 1:
        while not table.get_winner():
            continue
    table.finish()
    while input() != "exit":
        pass
