
A class called BuildersGame that represents the board for a two-player game that is played on a 5x5 grid. During the game, each players' builders will move around the board and add levels to towers. The winner is the first one to move a builder on top of a 3-story tower.

First, x places her two builders on the board, then o places her two builders on the board. Throughout the game, no two builders can ever occupy the same square.  After the initial placement, x can move either one of her builders to an adjacent square (one square orthogonally or diagonally). Builders can move any number of levels down, but can move at most 1 level up (they can also stay at the same level). Builders always move to the top of the tower on their destination square. After a builder moves, it **must** add a level to an adjacent square (it must be adjacent to the builder that moved). A level cannot be added to a square that is occupied by any builder. Once a tower has a 4th level, no further levels can be added. After x has moved and built, the players alternate moving and building in this way until the game ends. If a player moves one of her builders on top of a 3-story tower **or** if her opponent will not have a legal move available, then she has won.
