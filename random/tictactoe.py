class TicTacToe:
    """A class for TicTacToe Board. It keeps track of moves and declares winner, if any."""

    def __init__(self):
        """Initializing the board."""
        self._board = [[' ']*3 for i in range(3)]           # empty board
        self._player = 'X'                                  # total number of moves

    def move(self, i, j):
        """Making a move. Places either 'X' or 'O' in an empty board pos."""
        if not (0 <= i <=2 and 0 <= j <=2):
            raise ValueError("Invalid position.")
        if self._board[i][j] != ' ':
            raise ValueError("This position is occupied")
        elif self._player == 'X':
            self._board[i][j] = 'X'
            if self.winner() is not None:
                print(f"The game is complete and the winner is {self.winner()}.")
            else:
                self._player = 'O'
        else:
            self._board[i][j] = 'O'
            if self.winner() is not None:
                print(f"The game is complete and the winner is {self.winner()}.")
            else:
                self._player = 'X'

    def _is_win(self,mark):
        """Check whether the board configuration is a win for the given player."""
        board = self._board             # local variable for shorthand
        return (mark == board[0][0] == board[0][1] == board[0][2] or #row 0 
                mark == board[1][0] == board[1][1] == board[1][2] or #row 1 
                mark == board[2][0] == board[2][1] == board[2][2] or #row 2 
                mark == board[0][0] == board[1][0] == board[2][0] or #column 0 
                mark == board[0][1] == board[1][1] == board[2][1] or #column 1 
                mark == board[0][2] == board[1][2] == board[2][2] or #column 2 
                mark == board[0][0] == board[1][1] == board[2][2] or # diagonal 
                mark == board[0][2] == board[1][1] == board[2][0])   #rev diag

    def winner(self):
        """Return mark of winning player, or None to indicate a tie.""" 
        for mark in 'XO' :
            if self._is_win(mark): 
                return mark
        return None

    def __str__(self):
        """Prints the current board situation."""
        rows = ['|'.join(self._board[i]) for i in range(3)]
        return '\n-------\n'.join(rows)


def playTicTacToe():
    """This function asks for inputs from the players and let them play TicTacToe"""
    game = TicTacToe()
    tester = game.winner()
    dic = {'0' : (0, 0), '1' : (0, 1), '2' : (0, 2), '3' : (1, 0), '4' : (1,1), '5' : (1,2),
            '6' : (2, 0), '7' : (2, 1), '8' : (2,2)}
    while tester == None:
        entry = input("Please enter the number of your position.")
        i,j = dic[entry]
        game.move(i,j)
        tester = game.winner()
        print(str(game))

#####
if __name__ == "__main__":
    playTicTacToe()


