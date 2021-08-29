class BuildersGame:
    def __init__(self):
        """initializes the start of a game"""
        self._board = [
            ['N','N','N','N','N'],
            ['N','N','N','N','N'],
            ['N','N','N','N','N'],
            ['N','N','N','N','N'],
            ['N','N','N','N','N'],
            ]
        self._tower_board = [
            ['N','N','N','N','N'],
            ['N','N','N','N','N'],
            ['N','N','N','N','N'],
            ['N','N','N','N','N'],
            ['N','N','N','N','N'],
            ]
        self._current_state = "UNFINISHED"
        self._player_turn = "x"
        self._turn_number = 1

    def print_board(self):
        """prints board displaying builder positions"""
        
        print("  [ 0,   1,   2,   3,   4  ]")
        for index,row in enumerate(self._board):
            print(index,row)
        
    def print_tower_board(self):
        """prints board displaying tower levels"""

        print("  [ 0,   1,   2,   3,   4  ]")
        for index,row in enumerate(self._tower_board):
            print(index,row)

    def get_current_state(self):
        """returns the current state of the game
        this should return "X_WON", "O_WON", OR "UNFINISHED" """
        
        return self._current_state

    def get_player_turn(self):
        """returns the value of whose turn it is"""
        
        return self._player_turn

    def _set_player_turn(self):
        """changes the status of whose turn it is"""
        
        if self._player_turn == "x":
            self._player_turn = "o"
        
        else:
            self._player_turn = "x"
        
        self._turn_number += 1

    def is_unoccupied(self, target_row, target_col):
        """checks to make sure that the target position is unoccupied by
        another builder."""
         
        if self._board[target_row][target_col] == 'N':
            return True
        
        return False

    def is_adjacent(self, current_row, current_col, target_row, target_col):
        """tests whether a target coordinate is adjacent to the current one
        maybe use this method to clean up code as it has repeated in a couple
        of other methods"""
        
        if abs(target_row - current_row) > 1:
            return False
        if abs(target_col - current_col) > 1:
            return False
        
        return True

    def is_in_range(self, target_row, target_col):
        """checks to make sure that the desired move is on the board"""

        if target_row < 0 or target_row > 4:
            return False
        if target_col < 0 or target_col > 4:
            return False

        return True
    
    def is_tower_not_too_tall(self, current_row, current_col, target_row, target_col):
        """check whether the target position has a tower that is more than 1 level
        higher than the current position"""

        if self._tower_board[current_row][current_col] == "N":
            current_height = 0
        else:
            current_height = self._tower_board[current_row][current_col]

        if self._tower_board[target_row][target_col] == "N":
            target_height = 0
        else:
            target_height = self._tower_board[target_row][target_col]

        if target_height - current_height > 1:
            return True

    def is_move_legal(self, current_row, current_col, target_row, target_col):
        """checks to make sure the desired move is allowed"""

        if self.is_in_range(target_row, target_col) != True:
            return False
            
        if self.is_unoccupied(target_row, target_col) != True:
            return False
        
        if self.is_adjacent(current_row, current_col, target_row, target_col) != True:
            return False

        if self.is_tower_not_too_tall(current_row, current_col, target_row, target_col):
            return False

        #prevents moving a non existent piece
        if self._board[current_row][current_col] == 'N':
            return False

        return True

    def initial_placement(self, row_1, col_1, row_2, col_2, player):
        """initializes where each of the players' builders start
        on the board"""

        #makes sure player is making initialization on their turn    
        if player != self._player_turn:
            return False

        #prevents further initialization after both players initialized    
        if self._turn_number > 2:
            return False

        if not self.is_in_range(row_1, col_1):
            return False

        if not self.is_in_range(row_2, col_2):
            return False

        if self.is_unoccupied(row_1,col_1) != True:
            return False
            
        if self.is_unoccupied(row_2,col_2) != True:
            return False
        
        if row_1 == row_2:
            if col_1 == col_2:
                return False

        else:
            self._board[row_1][col_1] = player
            self._board[row_2][col_2] = player

        self._set_player_turn()
        return True

    def _set_current_state(self, move_row, move_col, build_row, build_col):
        """this method will evaluate if a move will put a builder on top of a
        3-story tower or if the opponent will not be able to make any more moves
        and then change the current state of the game
        if player cannot build, player loses"""
        
        #sets current player as winner if their builder moves to a 3 story tower
        if self._tower_board[move_row][move_col] == 3:
            if self._player_turn == 'x':
                self._current_state = "X_WON"
            else:
                self._current_state = "O_WON"
        else:
            self._current_state = "UNFINISHED"

    def make_move(self, current_row, current_col, move_row, move_col, build_row, build_col):
        """takes the current position of a builder, moves the builder
        to a new position and then build a level in an adjacent spot"""
        
        player = ""
        if self._current_state != "UNFINISHED":
            return False

        #this is to check that both players made initial placements first
        if self._turn_number < 3:
            return False

        if self.is_move_legal(current_row, current_col, move_row, move_col) == False:
            return False

        #this is to check that it is the current player's turn
        if self._board[current_row][current_col] == 'x':
            player = 'x'
        if self._board[current_row][current_col] == 'o':
            player = 'o'
        if player != self._player_turn:
            return False
        
        
        #This is check that tower is being built adjacent to the position that a builder just moved to
        if self.is_adjacent(move_row, move_col, build_row, build_col) == False:
            return False
        
        if self.is_in_range(build_row,build_col) != True:
            return False

        
        #this determines whether the current player is x or o based off of 
        # the current builder being moved    
        if player == 'x':
            self._board[move_row][move_col] = 'x'
        if player == 'o':
            self._board[move_row][move_col] = 'o'
        
        self._board[current_row][current_col] = 'N'
        """building tower level
        if the position is == "N" then that means a level has not been placed
        the string N should be changed to integer 1 so that it can be incremented
        otherwise, if the position has integer that means a tower exists
        and the integer should be incremented by 1 """
        if self._tower_board[build_row][build_col] == 'N':
            self._tower_board[build_row][build_col] = 1
        else:
            self._tower_board[build_row][build_col] += 1 
        
        self._set_current_state(move_row, move_col, build_row, build_col)
        self._set_player_turn()
        
        return True