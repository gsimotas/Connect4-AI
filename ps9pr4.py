#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ returns a string representing an AIPlayer object.
        """
        
        string = 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return string
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for 
            each column of the board, and that returns 
            the index of the column with the maximum score.
        """
        
        max_score = max(scores)
        max_index = []
        for col in range(len(scores)):
            if scores[col] == max_score:
                max_index += [col]
        
        if self.tiebreak == 'LEFT':
            return max_index[0]
        elif self.tiebreak == 'RIGHT':
            return max_index[-1]
        else:
            return random.choice(max_index)
        
    def scores_for(self, b):
        """ takes a Board object b and determines the 
            called AIPlayer‘s scores for the columns in b
        """
        
        scores = [50] * b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                p1 = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                p1_scores = p1.scores_for(b)
                
                if max(p1_scores) == 0:
                    scores[col] = 100
                elif max(p1_scores) == 50:
                    scores[col] = 50
                elif max(p1_scores) == 100:
                    scores[col] = 0
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """ returns the called AIPlayer‘s judgment of its best possible move.
        """
        
        scores = self.scores_for(b)
        move = self.max_score_column(scores)
        self.num_moves += 1
        
        return move

