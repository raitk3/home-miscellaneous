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


def ask_input(player):
	length = ''
	railroad_points = {
		0: 0,
		1: 1,
		2: 2,
		3: 4,
		4: 7,
		6: 15,
		8: 21,
	}
	while not (length.isdigit() or len(length) > 1 and length[0] == '-' and length[1:].isdigit()):
		length = input(f"{player} is building a train.\nHow long is the train? ")
		if length == '':
			print("Skip")
			return 0
		elif length.lower() == 'end':
			return 'end'
		elif length.lower() == 'station':
			if player.stations_left > 0:
				print(f'Subtracting cost of station from {player}.')
				player.stations_left -= 1
				return -cost_of_station
			else:
				print(f'{player} has no more stations!')
				return 0
	if length[0] == '-':
		print(f'Subtracting {length[1:]} points from {player}.')
		return int(length)
	number_of_points = railroad_points.get(int(length))
	if number_of_points:
		print(f'Train with a length of {length} is worth {number_of_points} points.\nAdding {player} {number_of_points} points.')
		return number_of_points
	else:
		print('Invalid length!')
		return ask_input(player)


def print_table(list_of_players, turn):
    table_list = ["╔", "║", "╟", "║", "╚"]
    for i, player in enumerate(list_of_players):
        name = player.name
        if i == turn:
            name = name.upper()
        cell_width = max(len(player.name), 5, len(str(player.score)))
        table_list[0] += '═' * (cell_width + 2) + "╦"
        table_list[1] += f" {name:>{cell_width}} ║"
        table_list[2] += '─' * (cell_width + 2) + "╫"
        table_list[3] += f" {player.score:>{cell_width}} ║"
        table_list[4] += '═' * (cell_width + 2) + "╩"
    table_list[0] = table_list[0][:-1] + "╗"
    table_list[2] = table_list[2][:-1] + "╢"
    table_list[4] = table_list[4][:-1] + "╝"
    return "\n".join(table_list)
	
def print_end_table(list_of_players):
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


def ask_number_of_players():
	number_of_players = input("How many players are there? ")
	while not number_of_players.isdigit() or int(number_of_players) > 5 or int(number_of_players) < 1:
		number_of_players = input("Insert the number of players (1-5)! ")
	return int(number_of_players)

def ask_names(number_of_players):
	players_list = list()
	for i in range(number_of_players):
		new_name = input(f"Player {i+1}:")
		players_list.append(Player(new_name))
	return players_list


def add_ten(players):
	while True:
		longest = input("Who got the longest continous railroad? ")
		for player in players:
			if player.name.capitalize() == longest.capitalize():
				print(f'Adding {player} 10 points for the longest continous railroad.')
				player.score += 10
				return True
		print("There's no such player!")

def ask_bonus(player):
	score = ''
	while not (score.isdigit() or len(score) > 1 and score[0] == '-' and score[1:].isdigit()):
		score = input(f"Task-points for {player}\nHow many extra points are awarded? ")
	return int(score)
	

def game_loop():
	number_of_players = ask_number_of_players()
	players = ask_names(number_of_players)
	turn = 0
	print(print_table(players, turn))
	while True:
		score = ask_input(players[turn])
		if score == 'end':
			break
		players[turn].add_points(score)
		turn = (turn + 1) % len(players)
		print("Scores:")
		print(print_table(players, turn))
	return players
	
	
def end(players):
	add_ten(players)
	for player in players:
		additional_score_for_tasks = ask_bonus(player)
		print(f"Adding {player} {additional_score_for_tasks} points.")
		player.score += additional_score_for_tasks
	print("Final scores:")
	print(print_end_table(players))
		
		
def main():
	while True:
		players = game_loop()
		end(players)
		
		input_text = ''
		print("Insert 'new game' to start a new game or Press Ctrl+C to exit.")
		
		while input_text != 'new game':
			input_text = input().lower()
	
    
	
if __name__ == '__main__':
    main()