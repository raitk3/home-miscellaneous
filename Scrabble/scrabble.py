class Player:
    def __init__(self, name):
        self.name = name.capitalize()
        self.score = 0

    def add_points(self, score):
        self.score += score

    def __repr__(self):
        return self.name


def ask_input(player):
    score = ''
    while not (score.isdigit() or len(score) > 1 and score[0] == '-' and score[1:].isdigit()):
        score = input(f"Kelle kord: {str(players[turn])}\nMitu punkti ta sai? ")
    return int(score)


def print_table(list_of_players):
	table_list = ["╔", "║", "╟" , "║", "╚"]
	for player in list_of_players:
		cell_width = max(len(player.name), 5, len(str(player.score)))
		table_list[0] += '═' * (cell_width + 2) + "╦"
		table_list[1] += f" {player.name:>{cell_width}} ║"
		table_list[2] += '─' * (cell_width + 2) + "╫"
		table_list[3] += f" {player.score:>{cell_width}} ║"
		table_list[4] += '═' * (cell_width + 2) + "╩"
	table_list[0] = table_list[0][:-1] + "╗"
	table_list[2] = table_list[2][:-1] + "╢" 
	table_list[4] = table_list[4][:-1] + "╝" 	
	return "\n".join(table_list)


if __name__ == '__main__':
    number_of_players = int(input("Mitu mängijat?"))
    players = []
    turn = 0
    for _ in range(number_of_players):
        new_name = input("Mis su nimi on?")
        players.append(Player(new_name))
    print("Hetkeseis:")
    print(print_table(players))
    while True:
        score = ask_input(players[turn])
        players[turn].add_points(score)
        turn = (turn + 1) % len(players)
        print("Hetkeseis:")
        print(print_table(players))
