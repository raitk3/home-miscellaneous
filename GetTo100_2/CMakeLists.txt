cmake_minimum_required(VERSION 3.15)
project(GetTo100_2)

set(CMAKE_CXX_STANDARD 14)

add_executable(GetTo100_2 main.cpp data.h game_logic.h game_logic.cpp display.h display.cpp)