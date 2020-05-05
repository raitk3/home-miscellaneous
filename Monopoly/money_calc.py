def parse_to_int(text):
    if not text[-1].isdigit():
        if text[-1] == "M":
            return parse_to_int(text[:-1]) * 1000000
        elif text[-1] == "k":
            return parse_to_int(text[:-1]) * 1000
    return float(text)



def money_to_text(money):
    if money // 1000000 != 0:
        return f"{money / 1000000}M"
    elif money // 1000 != 0:
        return f"{money / 1000}k"
    else:
        return str(money)

if __name__ == "__main__":
    money = 15000000
    while True:
        print(('\n' * 10) + f"Praegu sul on M{money_to_text(money)}")
        text = input("Sisesta summa: ")
        money += parse_to_int(text)