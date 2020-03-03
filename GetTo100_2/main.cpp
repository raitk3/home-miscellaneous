#include "game_logic.h"
#include "display.h"
#include "data.h"

Data init() {
    int age = get_age();
    Data data;
    data.age = age;
    return data;
}

bool game_loop(Data& data) {
    if (data.players_turn) {
        data = players_turn(data);
    } else {
        data = ai_turn(data);
    }
    display(data);
    return check_end(data);
}

int main() {
    Data data = init();
    print_rules();
    while (!game_loop(data));
    display_winner(data);
}