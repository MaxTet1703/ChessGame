from abc import ABC, abstractmethod
from ..board import chessfield, chessboard, move
from .color import Color


class IChessman(ABC):

    def __init__(
            self,
            position: chessfield.ChessField,
            color: Color,
    ) -> None:
        self.color = color
        self.position = position
        position.chessman = self

    @property
    def get_position(self):
        return self.position

    @abstractmethod
    def get_possible_moves(
            self,
            all_position: list[list[chessfield.ChessField]]
    ) -> list[list[chessfield.ChessField]]:
        pass

    def check_position_exists(
            self,
            new_position: chessfield.ChessField,
            all_positions: list[list[chessfield.ChessField]],
    ) -> bool:
        
        possible_moves = self.get_possible_moves(all_positions)
        return new_position in possible_moves

    def go_to_position(
            self,
            new_position: chessfield.ChessField,
            board: chessboard.ChessBoard,
    ) -> move.ChessMove:
        if not self.check_position_exists(new_position, board.board):
            raise ValueError("Values is not valid")

        chess_move = move.ChessMove(self.position, new_position)
        new_position.chessman = self
        self.position = new_position

        return chess_move