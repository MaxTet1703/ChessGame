from .chessfield import ChessField


class ChessBoard:

    def __init__(self):
        self.board = [[ChessField(row, col) for col in range(8)] for row in range(8)]
    
    def get_field(self, row, col):
        if not (0 <= row <= 7 and 0 <= col <= 7):
            return ValueError("Values is not correct") 
        return self.board[row][col]