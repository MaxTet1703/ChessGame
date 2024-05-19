from .ichessman import BaseChessman
from ..chess_field import ChessField


class Pawn(BaseChessman):

    available_steps = (
        (1, 0),
        (1, 1),
        (1, -1),
        (2, 0)
    )

    def new_position(self, row: int, col: int, chessfield: ChessField):
        if not super().new_position(row, col):
            raise ValueError("coord is out of filed")
        field = chessfield.get_cell(row, col)
        step = (self.get_position[0] - row,
                self.get_position[1] - col)
        if step not in self.available_steps:
            raise ValueError("Pawn cannot move like this")
        elif step in self.available_steps[1:3]:
            if not chessfield.get_cell(row, col).is_busy:
                raise ValueError("Pawn can move like this when there is a enemy chesman")
            elif field.is_busy and field.is_busy.color == field.is_busy.color:
                raise ValueError("Pawn cannot move to there, there is friendly chessman")
        elif step in self.available_steps[0:4:3]:
            if field.is_busy:
                raise ValueError("Pawn can move there there is chessman")
            elif step == self.available_steps[-1] and field.row not in (1, 6):
                raise ValueError("Pawn cannot do double movement it must be in start position")
        field.is_busy = self     
        self.row = row 
        self.col = col