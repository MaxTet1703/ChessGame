from unittest import TestCase

from ..chessmen import Knight, Queen, Color
from ..board.chessboard import ChessBoard


class TestKnight(TestCase):

    def setUp(self):
        self.board = ChessBoard()
        self.knight = Knight(self.board.get_field(2, 2), Color.WHITE)

    def test_side(self) -> None:
        assert self.knight.color == Color.WHITE
        assert self.knight.color != Color.BLACK

    def test_position(self):
        assert self.knight.position == self.board.get_field(2, 2)

    def test_move_position_free(self):
        new_position = self.board.get_field(4, 3)
        self.knight.go_to_position(new_position, self.board)
        assert self.knight.position == new_position
        assert new_position.chessman == self.knight
        self.board.get_field(4, 3).chessman = None

    def test_move_position_not_exist(self):
        with self.assertRaises(ValueError) as context:
            new_position = self.board.get_field(8, 0)
            self.knight.go_to_position(new_position, self.board)
            self.assertTrue(ValueError in context.exception)
            self.board.get_field(8, 0).chessman = None
    
    def test_move_position_not_free_allied(self):
        with self.assertRaises(ValueError) as context:
            new_position = self.board.get_field(4, 3)
            Queen(new_position, Color.WHITE,)
            self.knight.go_to_position(new_position, self.board)
            self.assertTrue(ValueError in context.exception)

    def test_move_position_enemy(self) -> None:
        new_position = self.board.get_field(4, 3)
        Queen(new_position, Color.BLACK)
        self.knight.go_to_position(new_position, self.board)
        assert self.knight.position == new_position
        assert new_position.chessman == self.knight