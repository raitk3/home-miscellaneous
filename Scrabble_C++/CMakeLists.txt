cmake_minimum_required(VERSION 3.15)
project(Scrabble_C__)

set(CMAKE_CXX_STANDARD 17)

add_subdirectory(test)
add_executable(Scrabble_C__
        src/main.cpp
        src/IO/InOut.cpp
        src/IO/InOut.h
        src/Player/Player.h
        src/game_logic/game_logic.cpp
        src/game_logic/game_logic.h
        src/game_logic/game_data.h
        src/game_logic/scores.h
        src/game_logic/scores.cpp src/main2.cpp)