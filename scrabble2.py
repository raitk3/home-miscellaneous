class Player:
    def __init__(self, name):
        self.name = name.capitalize()
        self.score = 0

    def add_points(self, score):
        self.score += score

    def __repr__(self):
        return self.name


def process_word(word):
    values = {'A': 1,
              'B': 4,
              'D': 2,
              'E': 1,
              'F': 8,
              'G': 3,
              'H': 4,
              'I': 1,
              'J': 4,
              'K': 1,
              'L': 1,
              'M': 2,
              'N': 2,
              'O': 1,
              'P': 4,
              'R': 2,
              'S': 1,
              'Š': 10,
              'Z': 10,
              'Ž': 10,
              'T': 1,
              'U': 1,
              'V': 3,
              'Õ': 4,
              'Ä': 5,
              'Ö': 6,
              'Ü': 5,
              ' ': 0}
    word = word.strip()
    multiplier = 1
    temp_score = 0
    if word[-1].isdigit():
        multiplier = int(word[-1])
        word = word[:-1]
    for ch in word:
        if ch in values:
            temp_score += values[ch]
        else:
            print(f"BUG?  '{ch}'-l pole väärtust.")
    total_score = temp_score * multiplier
    print()
    print(f'Sõna {word} andis {temp_score} punkti.')
    print(f'{temp_score}*{multiplier}={total_score}')
    return total_score


def ask_input(player):
    played_words = input(f"Kelle kord: {player}\nSisesta sõna(-d) või saadud skoor:").upper()
    score = 0
    try:
        score += int(played_words)
    except ValueError:
        played_words = played_words.split(",")
        for word in played_words:
            if len(word) > 1:
                score += process_word(word)
        print()
        print(f'Kogu saadud skoor on {score} punkti.')
    return score


def print_instructions():
    print(f'\nSisestada saab nii sõnu kui skoore.\n'
          f'Vale sisendi puhul ei tehta midagi ning kord läheb järgmisele mängijale.\n'
          f'Tühja ruudu puhul võib sisestada tühiku.'
          f'Kui mõni täht on kordistajal, siis tuleb sõnas kirjutada niimitu rohkem tähte.\n'
          f'Näiteks "ja" a-täht on x3 peal, siis tuleb kirjutada "jaaa".\n'
          f'Kui kogu sõna kordistatakse, siis kirjutada sõna lõppu vastav arv.\n'
          f'Näiteks "jaaa3".\n'
          f'Kui on mitu sõna, siis eraldada need komaga.\n'
          f'Näiteks "ja, aaga, ega3".')


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


def main():
    arv = input("Mitu mängijat?")
    while not arv.isdigit():
        arv = input("Mitu mängijat?")
    number_of_players = int(arv)
    players = []
    turn = 0
    for i in range(number_of_players):
        new_name = input(f"{i + 1}. mängija nimi:")
        players.append(Player(new_name))
    print_instructions()
    print("Hetkeseis:")
    print(print_table(players, turn))
    while True:
        score = ask_input(players[turn])
        players[turn].add_points(score)
        turn = (turn + 1) % len(players)
        print("Hetkeseis:")
        print(print_table(players, turn))


if __name__ == '__main__':
    while True:
        main()
