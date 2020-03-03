#pragma once

#include <utility>
#include <vector>
#include "../Player/Player.h"

struct GameData {
    std::vector<Player> players;
    int turn = 0;

    explicit GameData(std::vector<Player> inPlayers) {
        players = std::move(inPlayers);
    }
};