from unittest import TestCase

from ..chessmen import Knight, Queen, Color
from ..board.chessboard import ChessBoard


class TestGame(TestCase):

    def setUp(self):
        self.board = ChessBoard()

    def test_queen_take_knight(self) -> None:
        queen_white = Queen(self.board.get_field(0, 0), Color.WHITE)
        knight_black = Knight(self.board.get_field(2, 3), Color.BLACK)

        new_position = self.board.get_field(4, 4)
        queen_white.go_to_position(new_position, self.board)
        assert queen_white.position == new_position
        assert new_position.chessman == queen_white

        new_position = self.board.get_field(4, 2)
        knight_black.go_to_position(new_position, self.board)
        assert knight_black.position == new_position
        assert new_position.chessman == knight_black

        new_position = self.board.get_field(4, 2)
        queen_white.go_to_position(new_position, self.board)
        assert queen_white.position == new_position
        assert new_position.chessman == queen_white
    
    def test_knight_take_queen(self):
        queen_white = Queen(self.board.get_field(0, 0), Color.WHITE)
        knight_black = Knight(self.board.get_field(2, 1), Color.BLACK)
        new_position = self.board.get_field(0, 0)
        assert new_position.chessman == queen_white
        knight_black.go_to_position(new_position, self.board)
        assert new_position.chessman == knight_black

    def test_knight_take_knight(self):
        knight_white = Knight(self.board.get_field(0, 0), Color.WHITE)
        knight_black = Knight(self.board.get_field(2, 1), Color.BLACK)
        new_position = self.board.get_field(0, 0)
        assert new_position.chessman == knight_white
        knight_black.go_to_position(new_position, self.board)
        assert new_position.chessman == knight_black

    def test_queen_take_queen(self):
        queen_white = Queen(self.board.get_field(0, 0), Color.WHITE)
        queen_black = Queen(self.board.get_field(7, 7), Color.BLACK)
        new_position = self.board.get_field(0, 0)
        assert new_position.chessman == queen_white
        queen_black.go_to_position(new_position, self.board)
        assert new_position.chessman == queen_black

    def test_queen_take_queen_same_color(self):
        queen_white = Queen(self.board.get_field(0, 0), Color.WHITE)
        other_queen = Queen(self.board.get_field(7, 7), Color.WHITE)
        new_position = self.board.get_field(0, 0)
        assert new_position.chessman == queen_white
        with self.assertRaises(ValueError) as context:
            other_queen.go_to_position(new_position, self.board)
            self.assertTrue(ValueError in context.exception)

    def test_knight_take_knight_same_color(self):
        knight_white = Knight(self.board.get_field(0, 0), Color.WHITE)
        other_knight = Knight(self.board.get_field(1, 2), Color.WHITE)
        new_position = self.board.get_field(0, 0)
        assert new_position.chessman == knight_white
        with self.assertRaises(ValueError) as context:
            other_knight.go_to_position(new_position, self.board)
            self.assertTrue(ValueError in context.exception)