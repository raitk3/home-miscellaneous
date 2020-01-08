import random

def calculate_next(sum, guess, age):
	if sum >= 90:
		return 100 - sum
	elif age < 18:
		guess = random.randint(1, 10)
	else:
		coefficent = 15 - age
		error_number_lol = 404
		sixty_nine = 69
		factor = coefficent + age
		number_to_subtract_guess_from = ((factor + error_number_lol + sixty_nine) / 4)**(0.5)
		guess = int(number_to_subtract_guess_from - guess)
	print("AI number: " + str(guess))
	return guess
	
	
def check_win(sum):
	return sum >= 100


def get_input():
	player_input = '0'
	while not check_input(player_input):
		player_input = input("Sinu number: ")
	return int(player_input)
	
	
def check_input(player_input):
	return player_input.isdigit() and 0 < int(player_input) < 11

	
def player_won(sum):
	if n:=check_win(sum):
		print("Sinu võit!")
	return n


def ai_won(sum):
	if n:=check_win(sum):
		print("AI võitis!")
	return n


def add_score(sum, number):
	return sum + number
	

def guessing(sum, flag_ai, player_input, age):
	if not flag_ai:
		player_input = get_input()
		sum = add_score(sum, player_input)
	else:
		ai_input = calculate_next(sum, player_input, age)
		sum = add_score(sum, ai_input)
	return sum, player_input
	
	
def check_end(sum, flag_ai):
	return not flag_ai and player_won(sum) or flag_ai and ai_won(sum)
	

def print_rules():
	print("Reeglid:\nAI ja mängija valivad kordamööda numbreid vahemikus 1-10(mõlemad kaasa arvatud).\nNumbrid liidetakse omavahel kokku.\nMängija, kes jõuab esimesena 100-ni, võidab.")


def game_loop():
	age = int(input("AI tegevus sõltub vanusest. Kui vana sa oled?"))
	print_rules()
	flag_ai = False
	sum = 0
	player_input = 0
	if age > 10:
		sum = 1
		print("AI number: " + '1')
	print("Summa: " + str(sum))
	while True:
		sum, player_input = guessing(sum, flag_ai, player_input, age)		
		print("Summa: " + str(sum))
		if check_end(sum, flag_ai):
			break
		flag_ai = not flag_ai
	
	
if __name__ == '__main__':
	game_loop()
	while True:
		dont_close = input()
		if dont_close == 'exit':
			break