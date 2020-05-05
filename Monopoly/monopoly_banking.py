import copy

class Bank:
    people = []
    transactions_list = []
    
    def __init__(self):
        super().__init__()
    
    def transaction(self, player1, player2, money):
        if player1.money >= money:
            player1.money -= money
            player2.money += money
            self.transactions_list.append(f"{player1.name} gave M{money_to_string(money)} to {player2.name}.")
        else:
            print(f"{player1.name} pole piisavalt raha!")            
        
    def find_person(self, name):
        if name == "Bank":
            rich_boi = Person("Bank")
            rich_boi.money = 999999999
            return rich_boi
        for person in self.people:
            if person.name == name:
                return person
        return None
    def __repr__(self):
        return "\n".join([str(person) for person in self.people])

class Person:
    money = 0
    name = ""
    def __init__(self, name):
        self.name = name.title()
        self.money = 15000000
    
    def __str__(self):
        return f"{self.name}: M{money_to_string(self.money)}"

    def __repr__(self):
        return f"{self.name}: M{self.money}"


def init(bank):
    number = int(input("Mängijate arv: "))
    for i in range(number):
        name = input(f"Mängija {i+1} nimi: ").title()
        bank.people.append(Person(name))
    return bank

def money_to_string(money):
    if money // 1000000 != 0:
        return f"{money / 1000000}M"
    elif money // 1000 != 0:
        return f"{money / 1000}k"
    else:
        return str(money)

def string_to_money(text):
    if not text[-1].isdigit():
        if text[-1] == "M":
            return string_to_money(text[:-1]) * 1000000
        elif text[-1] == "k":
            return string_to_money(text[:-1]) * 1000
    return float(text)


def parse_input(bank, transaction):
    try:
        copy_bank = copy.deepcopy(bank)
        person_1_name = transaction.split(",")[0].strip().title()
        person_2_name = transaction.split(",")[1].strip().title()
        amount = string_to_money(transaction.split(",")[2].strip())
        person_1 = copy_bank.find_person(person_1_name)
        person_2 = copy_bank.find_person(person_2_name)
        if person_1 and person_2:
            copy_bank.transaction(person_1, person_2, amount)
        return copy_bank
    except:
        print("Wrong input!")
        return bank


if __name__ == "__main__":
    bank = init(Bank())
    print(bank)
    while True:
        transaction = input()
        if transaction.lower() == "transactions":
            print(*bank.transactions_list, sep="\n")
        else:
            bank = parse_input(bank, transaction)
        print("\n" * 10 + str(bank))
