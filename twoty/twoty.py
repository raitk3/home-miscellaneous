numbers = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
tens2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

def parse_three_digits(number):
    hundred = int(number / 100)
    one = int(number % 10)
    ten = int((number % 100 - one) / 10)
    text = ""
	
    if hundred > 0:
        text += numbers[hundred] + " hundred"
    
	
    if hundred > 0 and number % 100 > 0:
        text += " ";

    if ten == 1:
        return text + tens2[one]
    elif ten > 0:
        text += tens[ten]
        if one == 0:
            return text
        else:
            text += "-" + numbers[one]
    else:
        return text + numbers[one]
    return text

def get_string(number, three_blocks):
    text = ""
    print(number)
    if number == 0 and three_blocks == 0:
        return "nil"
    if number > 999:
        text += get_string(number//1000, three_blocks + 1)
        if (number//1000) % 1000 != 0:
            if three_blocks == 0:
                    text += " thousand "
            elif three_blocks == 1:
                    text += " million "
            elif three_blocks == 2:
                    text += " billion "
            elif three_blocks == 3:
                    text += " trillion "
            elif three_blocks == 4:
                    text += " quadrillion "
            elif three_blocks == 5:
                    text += " quintrillion "
            elif three_blocks == 6:
                    text += " sextillion "
            elif three_blocks == 7:
                    text += " septillion "
            elif three_blocks == 8:
                    text += " octillion "
            elif three_blocks == 9:
                    text += " nonillion "
            elif three_blocks == 10:
                    text += " decillion "
    text += parse_three_digits(number % 1000)
    return text


if __name__ == '__main__':
    while True:
        i = int(input("Insert a number!"))
        print(f"{i}: {get_string(i, 0)}")