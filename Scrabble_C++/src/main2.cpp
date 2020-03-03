#include "game_logic/scores.h"

int main2() {
    for (std::pair<const std::basic_string<char, std::char_traits<char>, std::allocator<char>>, int> entry: scoreboard) {
        std::cout << entry.first << ": " << entry.second << std::endl;
    }
    return 0;
}