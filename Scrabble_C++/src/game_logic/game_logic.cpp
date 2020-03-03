#include <iostream>

#include "game_logic.h"



GameData turn(GameData data) {
    Player current_player = data.players[data.turn];
    int score = ask_score(current_player);
    current_player.score += score;
    data.players[data.turn] = current_player;
    data.turn += 1;
    data.turn %= data.players.size();
    return data;
}

