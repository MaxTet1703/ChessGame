from .ichessman import IChessman
from ..board import chessfield


class Knight(IChessman):

    def add_move(
        self,
        position: chessfield.ChessField,
        moves: list[chessfield.ChessField],
    ) -> None:
        chessman = position.chessman
        if not chessman or (chessman and chessman.color != self.color):
            moves.append(position)

    def get_possible_moves(
            self,
            all_position: list[list[chessfield.ChessField]]
    ) -> list[list[chessfield.ChessField]]:
        moves = []
        x = self.position.col
        y = self.position.row

        j = 2
        for i in range(1, 3):
            if x - i > -1 and y + j < 8:
                self.add_move(all_position[y + j][x - i], moves)
            if x - i > -1 and y - j > -1:
                self.add_move(all_position[y - j][x - i], moves)
            if x + i < 8 and y + j < 8:
                self.add_move(all_position[y + j][x + i], moves)
            if x + i < 8 and y - j > -1:
                self.add_move(all_position[y - j][x + i], moves)
            j -= 1
        return moves