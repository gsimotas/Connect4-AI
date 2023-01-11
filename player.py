

from board import Board

# write your class below.
class Player:
    def __init__(self, checker):
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """ returns a string representing a Player object.
        """
        return 'Player ' + self.checker
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker of the Player object’s opponent.
        """
        if self.checker == 'O':
            return 'X'
        else:
            return 'O'
    
    def next_move(self, b):
        """ Get a next move for this player that is valid
        for the board b.
        """
        
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try Again!\n')

                
                
    
