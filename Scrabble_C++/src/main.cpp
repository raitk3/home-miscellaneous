#include <iostream>

#include "IO/InOut.h"
#include "game_logic/game_data.h"
#include "game_logic/game_logic.h"

int main2() {
    int numberOfPlayers = ask_number_of_players();
    std::vector<Player> players;
    std::cout << "Number of players: " << numberOfPlayers << std::endl;
    for (int i = 0; i < numberOfPlayers; i++) {
        std::cout << "Insert the name for player " << i+1 << "." << std::endl;
        std::string name = ask_name();
        Player player(name);
        players.push_back(player);
    }
    GameData data = GameData(players);
    print_table(data.players);

    while (true) {
        data = turn(data);
        print_table(data.players);
    }
}
