#pragma once

#include <string>

struct Player {
    std::string name = "";
    int score = 0;

    Player(std::string newName) {
        name = newName;
    }
};

