#include "display.h"

void print_rules() {
    std::cout <<
    "Player and AI take turns picking numbers 1-10(incl.)." << std::endl
    << "All of the numbers will be summed." << std::endl
    << "First to get to 100 wins." << std::endl;
}

void display(Data data) {
    std::cout << "Sum: " << data.sum << std::endl;
}

void display_winner(Data data) {
    if (data.players_turn) std::cout << "AI won!" << std::endl;
    else std::cout << "You won!" << std::endl;
}
