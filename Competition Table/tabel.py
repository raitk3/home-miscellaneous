
class Table:
    teams = []
    team_names = {}
    games = {}

    def __init__(self):
        number_of_teams = int(input("Number of teams: "))
        for i in range(number_of_teams):
            name = input(f"Team {i+1}: ")
            self.teams.append(Team(name))
            self.team_names[name] = i
    
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
            if f"{team_1_name} - {team_2_name}" not in self.games and f"{team_2_name} - {team_1_name}" not in self.games:
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

        except:
            print("Wrong input!")


    def get_games(self):
        return [f"{game} {self.games[game]}" for game in self.games]

    def print_games(self):
        print(*self.get_games(), sep="\n")

    def get_table(self):
        list_of_printable_lines = []
        list_of_writable_lines = []
        sorted_table = sorted(self.teams, key=lambda x: [x.get_score(), x.rounds_won], reverse = True)
        longest_name = max(max([len(name) for name in [el for el in self.team_names]]), 4)
        
        writable_separator = f"+{'':->{longest_name+2}}+{'':->3}+{'':->4}+{'':->4}+{'':->4}+{'':->4}+{'':->4}+{'':->5}+{'':->4}+"
        
        list_of_printable_lines.append(f"╔{'':═>{longest_name+2}}╦{'':═>3}╦{'':═>4}╤{'':═>4}╤{'':═>4}╦{'':═>4}╤{'':═>4}╤{'':═>5}╦{'':═>4}╗")
        list_of_printable_lines.append(f"║ {'Nimi': >{longest_name}} ║ {'M':>1} ║ {'Võ':>2} │ {'Vi':>2} │ {'K':>2} ║ {'VR':>2} │ {'KR':>2} │ {'RS':>3} ║ {'P':>2} ║")
        list_of_printable_lines.append(f"╠{'':═>{longest_name+2}}╬{'':═>3}╬{'':═>4}╪{'':═>4}╪{'':═>4}╬{'':═>4}╪{'':═>4}╪{'':═>5}╬{'':═>4}╣")
        
        list_of_writable_lines.append(writable_separator)
        list_of_writable_lines.append(f"| {'Nimi': >{longest_name}} | {'M':>1} | {'Võ':>2} | {'Vi':>2} | {'K':>2} | {'VR':>2} | {'KR':>2} | {'RS':>3} | {'P':>2} |")
        
        for i, team in enumerate(sorted_table):
            if i != 0:
                list_of_printable_lines.append(f"╟{'':─>{longest_name+2}}╫{'':─>3}╫{'':─>4}┼{'':─>4}┼{'':─>4}╫{'':─>4}┼{'':─>4}┼{'':─>5}╫{'':─>4}╢")
            
            list_of_printable_lines.append(f"║ {team.name: >{longest_name}} ║ {team.get_games():>1} ║ {team.wins:>2} │ {team.draws:>2} │ {team.defeats:>2} ║ {team.rounds_won:>2} │ {team.rounds_lost:>2} │ {team.get_round_diff():>3} ║ {team.get_score():>2} ║")
            
            list_of_writable_lines.append(writable_separator)
            list_of_writable_lines.append(f"| {team.name: >{longest_name}} | {team.get_games():>1} | {team.wins:>2} | {team.draws:>2} | {team.defeats:>2} | {team.rounds_won:>2} | {team.rounds_lost:>2} | {team.get_round_diff():>3} | {team.get_score():>2} |")
        
        list_of_printable_lines.append(f"╚{'':═>{longest_name+2}}╩{'':═>3}╩{'':═>4}╧{'':═>4}╧{'':═>4}╩{'':═>4}╧{'':═>4}╧{'':═>5}╩{'':═>4}╝")
        list_of_writable_lines.append(writable_separator)
        
        return list_of_printable_lines, list_of_writable_lines

    def print_table(self):
        print(*self.get_table()[0], sep="\n")

    def get_end(self):
            for team in self.teams:
                if team.get_games() != len(self.teams) - 1:
                    return False
            return True

    def finish(self):
        with open("results.txt", "w") as file:
            file.writelines("\n".join(self.get_table()[1]))
            file.write("\n")
            file.writelines("\n".join(self.get_games()))
        self.print_table()
        self.print_games()
    
            

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




if __name__ == "__main__":
    table = Table()
    while not table.get_end():
        table.print_table()
        input_string = input()
        table.parse_input(input_string)
    table.finish()
    while input() != "exit":
        pass
