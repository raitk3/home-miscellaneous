#pragma once

#include <iostream>
#include <vector>

#include "../Player/Player.h"
#include "../game_logic/game_logic.h"

int ask_number_of_players();

std::string ask_name();

void print_table(const std::vector<Player>& players);

int ask_score(Player player);