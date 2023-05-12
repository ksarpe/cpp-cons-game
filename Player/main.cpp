#include "board.h"
#include "game.h"
#include <string>

int main(int argc, char **argv){

    float timeDuration = argc == 5 ? std::stof(argv[4]) : 5f;
    Game game(timeDuration);

    std::string command;
    while (std::getline(std::cin, command)) {
        if (command == "start") {
            // It's this player's turn, so do some actions

            // When the actions are done, send "done" back to the Mediator
            std::cout << 0 << std::endl;
        }
}

    return 0;
}