#include "InOut.h"

#include <algorithm>

int ask_number_of_players() {
    /*
     * Ask number of players.
     * Return: int, number of players.
     */
    int numOfPlayers = 0;
    while (numOfPlayers < 2 || numOfPlayers > 5) {
        std::cout << "Insert the number of players!" << std::endl;
        std::cin >> numOfPlayers;
    }
    return numOfPlayers;
}

std::string ask_name() {
    std::string name;
    std::cin >> name;
    return name;
}

void print_table(const std::vector<Player>& players) {
    std::string row1 = "+";
    std::string row2 = "|";
    std::string row3 = "+";
    std::string row4 = "|";
    std::string row5 = "+";
    for (auto & player : players) {
        int name_length = player.name.length();
        int score_length = std::to_string(player.score).length();
        int width = std::max(5, std::max(name_length, score_length));
        row1 += std::string(width + 2, '-') + "+";
        row2 += std::string(width - player.name.length() + 1, ' ') + player.name + " |";
        row3 += std::string(width + 2, '-') + "+";
        row4 += std::string(width - score_length + 1, ' ') + std::to_string(player.score) + " |";
        row5 += std::string(width + 2, '-') + "+";
    }
    std::cout << row1 << std::endl
    << row2 << std::endl
    << row3 << std::endl
    << row4 << std::endl
    << row5 << std::endl;
}

int ask_score(Player player) {
    std::string score;
    std::cout << "It's " << player.name << "'s turn. Insert score!" << std::endl;
    std::cin >> score;

    if (std::all_of(score.begin(), score.end(), ::isdigit)) return std::stoi(score);
    else return get_score(score);
}
