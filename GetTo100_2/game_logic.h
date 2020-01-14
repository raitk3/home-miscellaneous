#pragma once

#include <iostream>
#include <cstdlib>
#include <ctime>

#include "data.h"

int get_age();

bool check_end(Data data);

int calculate_next(Data data);

Data players_turn(Data data);

Data ai_turn(Data data);