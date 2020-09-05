import json

def get_text(filename):
    text = ""
    with open(filename, "r", encoding="utf-8") as file:
        while True:
            c = file.read(1)
            if not c:
                break
            text += c
    return text

def get_dict(filename):
    with open(filename, "r", encoding='utf-8') as file:
        return json.load(file)

def replace_stuff(text, replace_map):
    new_text = ""
    for letter in text:
        if letter.lower() in replace_map:
            if letter.islower():
                new_text += replace_map[letter]
            else:
                new_text += replace_map[letter.lower()].upper()
        else:
            new_text += letter
    return new_text

def write_new(new_text):
    with open("new_text.txt", "w") as file:
        file.write(new_text)

if __name__ == '__main__':
    replace_map = get_dict("replacemap.json")
    text = get_text("esialgne_tekst.txt")
    print(text)
    print(replace_map)
    new_text = replace_stuff(text, replace_map)
    write_new(new_text)
    print(new_text)