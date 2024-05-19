from .chessfield.cell import ChessCell


class ChessFiled:

    def __init__(self):
        self.board = [[ChessCell(row, col) for col in range(8)] for row in range(8)]
    
    def get_cell(self, row, col):
        if not ( 0 <= row <= 7 and 0 <= col <=7):
            return None 
        return self.board[row][col]