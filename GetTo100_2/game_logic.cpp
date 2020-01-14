#include "game_logic.h"

int rand(int i, int i1);

int get_age() {
    int age;
    std::cout << "Actions of the AI depends on your age. How old are you?" << std::endl;
    std::cin >> age;
    return age;
}

bool check_end(Data data) {
    return data.sum >= 100;
}

int calculate_next(Data data) {
    if (data.sum > 89) {
        return 100 - data.sum;
    } else if (data.age <= 10) {
        srand(time(nullptr));
        return rand() % 10 + 1;
    } else {
        int current = data.sum;
        int guess = 0;
        while (true) {
            guess++;
            current++;
            if (guess == 10 || (current - 1) % 11 == 0) return guess;
        }
    }
}


Data players_turn(Data data) {
    Data data_copy = data;
    int next = 0;
    while (next < 1 || next > 10) {
        std::cout << "What's your next number?" << std::endl;
        std::cin >> next;
    }
    std::cout << "Your number was " << next << std::endl;
    data_copy.sum += next;
    data_copy.players_turn = false;
    return data_copy;
}

Data ai_turn(Data data) {
    Data data_copy = data;
    int next = calculate_next(data);
    std::cout << "AIs number is " << next << std::endl;
    data_copy.sum += next;
    data_copy.players_turn = true;
    return data_copy;
}