EMPTY = ' '
SHIP = '░'
HIT = '▒'
SUNK = '▓'
MISS = 'X'
ships = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
def generate_field():
	return [[EMPTY for _ in range(10)] for _ in range(10)]
	
	
def add_ship(field, coords1, coords2):
	row_1 = int(coords1[1:]) - 1
	row_2 = int(coords2[1:]) - 1
	col_1 = ord(coords1[0]) - 65
	col_2 = ord(coords2[0]) - 65
	if (row_1 == row_2 or col_1 == col_2) and check_ship(field, row_1, row_2, col_1, col_2):
		for row in range(min(row_1, row_2), max(row_1, row_2) + 1):
			for square in range(min(col_1, col_2), max(col_1, col_2) + 1):
				field[row][square] = SHIP
	return field


def check_ship(field, row_1, row_2, col_1, col_2):
	if abs(row_1 - row_2) < 5 and abs(col_1 - col_2) < 5:
		for row in range(max(0, min(row_1 - 1, row_2 - 1)), min(max(row_1 + 2, row_2 + 2), 10)):
				for square in range(max(0, min(col_1 - 1, col_2 - 1)), min(max(col_1 + 2, col_2 + 2), 10)):
					if field[row][square] != EMPTY:
						print(row, square)
						print(field[row][square])
						print('EMPTY FAILS!')
						print('CHECK FAILS!')
						return False
		ship_size = max(abs(row_1 - row_2) + 1, abs(col_1 - col_2) + 1)
		if ship_size in ships:
			ships.remove(ship_size)
			return True
		else:
			print('EI SAA SEDA LAEVA PANNA!')
	print('CHECK FAILS!')
	return False


def hit(field, coords):
	row = int(coords[1:]) - 1
	col = ord(coords[0]) - 65
	field[row][col] = HIT
	return field
	
	
def miss(field, coords):
	row = int(coords[1:]) - 1
	col = ord(coords[0]) - 65
	field[row][col] = MISS
	return field


def sink_ship(field, coords, cache=list()):
	row = int(coords[1:]) - 1
	col = ord(coords[0]) - 65
	field[row][col] = SUNK
	for i in range(max(0, row - 1), min(10, row + 2)):
		for j in range(max(0, col - 1), min(10, col + 2)):
			if (i, j) in cache:
				pass
			elif field[i][j] == HIT:
				cache.append((i, j))
				sink_ship(field, chr(j+65)+str(i+1), cache)
				field[i][j] = SUNK
			elif field[i][j] == EMPTY:
				field[i][j] = MISS
	return field
	
	
def print_field(my_field, enemy_field):
	print('  ABCDEFGHIJ ABCDEFGHIJ ')
	for i, row in enumerate(my_field):
		string_to_print = f"{i+1:>2}"
		for square in row:
			string_to_print += square
		string_to_print += "|"
		for square in enemy_field[i]:
			string_to_print += square
		string_to_print += str(i+1)
		print(string_to_print)
	print('  ABCDEFGHIJ ABCDEFGHIJ ')


def get_count(what_to_count, field):
	count = 0
	for row in field:
		for square in row:
			if square == what_to_count:
				count += 1
	return count

def check_end(my_field, enemy_field):
	return get_count(SUNK, my_field) == 20 or get_count(SUNK, enemy_field) == 20


def players_turn(my_field, enemy_field):
	action = ''
	while action != 'miss':
		square_to_put = input('Mis ruut?').upper()
		action = input('Mis juhtus?').lower()
		if action == 'hit':
			enemy_field = hit(enemy_field, square_to_put)
		elif action == 'sunk':
			enemy_field = sink_ship(enemy_field, square_to_put)
		elif action == 'miss':
			enemy_field = miss(enemy_field, square_to_put)
		print_field(my_field, enemy_field)

def get_square(field, coords):
	row = int(coords[1:]) - 1
	col = ord(coords[0]) - 65
	return field[row][col]
	

def opponents_turn(my_field, enemy_field):
	print('Vastase käik')
	missed = False
	while not missed:
		square_to_put = input('Mis ruut?').upper()
		type = get_square(my_field, square_to_put)
		if type == HIT:
			my_field = hit(my_field, square_to_put)
		elif type == EMPTY:
			my_field = miss(my_field, square_to_put)
			missed = True
	print_field(my_field, enemy_field)
	
	
def play():
	my_field = generate_field()
	enemy_field = generate_field()
	print_field(my_field, enemy_field)
	while get_count(SHIP, my_field) != 20:
		ship_coords = input("Kuhu panna laev? Ots1-Ots2: ").upper().split('-')
		if len(ship_coords) == 1:
			ship_coords.append(ship_coords[0])
		my_field = add_ship(my_field, ship_coords[0], ship_coords[1])
		print_field(my_field, enemy_field)
	while not check_end(my_field, enemy_field):
		players_turn(my_field, enemy_field)
		opponents_turn(my_field, enemy_field)
	if get_count(SUNK, my_field) == 20:
		print('Vastane võitis!')
	else:
		print('Sinu võit!')

if __name__ == '__main__':
	play()