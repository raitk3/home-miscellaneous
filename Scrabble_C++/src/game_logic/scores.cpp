#include "scores.h"

int get_score(const std::string& word) {
    int score = 0;
    for (int i = 0; i < word.length(); i++) {
        std::string character = word.substr(i, 1);
        if (scoreboard.count(character)) {
            std::cout << character << ": " << scoreboard.at(character) << std::endl;
            score += scoreboard.at(word.substr(i, 1));
        } else {
            std::cout << character << " has no score..." << std::endl;
        }
    }
    return score;
}
