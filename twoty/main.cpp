#include <iostream>
#include <map>

std::map<int, std::string> numbers {
        {0, ""},
        {1, "one"},
        {2, "two"},
        {3, "three"},
        {4, "four"},
        {5, "five"},
        {6, "six"},
        {7, "seven"},
        {8, "eight"},
        {9, "nine"}
};

std::map<int, std::string> tens {
        {0, ""},
        {1, "ten"},
        {2, "twenty"},
        {3, "thirty"},
        {4, "forty"},
        {5, "fifty"},
        {6, "sixty"},
        {7, "seventy"},
        {8, "eighty"},
        {9, "ninety"}
};

std::map<int, std::string> tens2 {
        {0, "ten"},
        {1, "eleven"},
        {2, "twelve"},
        {3, "thirteen"},
        {4, "fourteen"},
        {5, "fifteen"},
        {6, "sixteen"},
        {7, "seventeen"},
        {8, "eighteen"},
        {9, "nineteen"}
};

std::string parse_three_digits(int number) {
    int hundred = number / 100;
    int one = number % 10;
    int ten = (number % 100 - one) / 10;

    std::string text;
    if (hundred > 0) {
        text += numbers.at(hundred) + " hundred";
    }
    if (hundred > 0 && number % 100 > 0) {
        text += " and ";
    }
    if (ten == 1) {
        return text + tens2.at(one);
    } else if (ten > 0) {
        text += tens.at(ten);
        if (one == 0) {
            return text;
        } else {
            text += " " + numbers.at(one);
        }
    } else {
        return text + numbers.at(one);
    }
    return text;
}

std::string get_string(int number, int three_blocks) {
    std::string text;
    if (number == 0 and three_blocks == 0) return "nil";
    if (number > 999) {
        text += get_string(number/1000, three_blocks++);
        switch (three_blocks) {
            case 1:
                text += " thousand ";
                break;
            case 2:
                text += " million ";
                break;
            case 3:
                text += " billion ";
                break;
            case 4:
                text += " trillion ";
                break;
            default:
                break;
        }
    }
    text += parse_three_digits(number % 1000);
    return text;
}


int main() {
    for(int i = 0; i < 100000; i++) {
        std::cout << i << ": " << get_string(i, 0) << std::endl;
    }
}
