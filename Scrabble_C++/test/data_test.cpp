#include "../src/Player/Player.h"
#include "../src/game_logic/game_data.h"
#include "gtest/gtest.h"

TEST(GameData, given2Players_generateData_check2PlayersInData) {
    std::vector<Player> players = {Player("Player1"), Player("Player2")};

    GameData data = GameData(players);

    ASSERT_EQ(data.players.size(), 2);
}