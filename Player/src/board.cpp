#include "board.h"
#include <fstream>
#include <sstream>


void Board::loadFromFile(const std::string& filename) {
     std::ifstream inputFile(filename);

    if (!inputFile.is_open()) {
        std::cout<<"Error opening file: "<<filename<<std::endl;
        return;
    }

    std::string line;
    std::vector<std::vector<char>> tempGrid;

    while (std::getline(inputFile, line)) {
        std::istringstream lineStream(line);
        std::vector<char> row;

        char cell;
        while (lineStream >> cell) {
            row.push_back(cell);
        }

        tempGrid.push_back(row);
    }

    inputFile.close();

    height = static_cast<int>(tempGrid.size());
    width = static_cast<int>(tempGrid[0].size());
    grid = tempGrid;
}

// void Board::print() const {
//     for (int i = 0; i < height; i++) {
//         for (int j = 0; j < width; ++j) {
//             std::cout << grid[i][j] << ' ';
//         }
//         std::cout << std::endl;
//     }
// }

