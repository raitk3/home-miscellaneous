#include "../src/game_logic/scores.h"
#include "gtest/gtest.h"

TEST(Scores, givenWord_callGetScore_returnFourPoints) {
    std::string wordToScore = "aaaa";

    int scoreToGive = get_score(wordToScore);

    ASSERT_EQ(scoreToGive, 4);
}