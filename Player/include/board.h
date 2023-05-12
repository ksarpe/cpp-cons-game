#ifndef BOARD_H
#define BOARD_H

#include <vector>
#include <iostream>

class Board{

public:
    void loadFromFile(const std::string& filename);
    //void print() const;
    char getCell(int x, int y) const {return grid[x][y];}

private:
    int width;
    int height;
    std::vector<std::vector<char>> grid;

};

#endif //BOARD_H