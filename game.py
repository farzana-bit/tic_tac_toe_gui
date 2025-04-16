class TicTacToeGame:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None

    def make_move(self, row, col):
        if self.board[row][col] == "" and self.winner is None:
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.winner = self.current_player
            elif self.check_draw():
                self.winner = "Draw"
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    def check_winner(self, row, col):
        b = self.board
        player = self.current_player
        #check row, column, and diagonals

        return(
            all(b[row][i] == player for i in range(3)) or
            all(b[i][col] == player for i in range(3)) or
            all(b[i][i] == player for i in range(3)) or
            all(b[i][2-i] == player for i in range(3))
        )
    
    def check_draw(self):
        return all(cell in ["X", "O"] for row in self.board for cell in row)
    
    def reset_game(self):
        self.__init__()