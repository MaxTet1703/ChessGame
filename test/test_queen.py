from unittest import TestCase

from ..chessmen import Knight, Queen, Color
from ..board.chessboard import ChessBoard


class TestQueen(TestCase):

    def setUp(self):
        self.board = ChessBoard()
        self.queen = Queen(self.board.get_field(2, 2), Color.WHITE)

    def test_side(self) -> None:
        assert self.queen.color == Color.WHITE
        assert self.queen.color != Color.BLACK

    def test_position(self) -> None:
        assert self.queen.position == self.board.get_field(2, 2)

    def test_move_position_free(self) -> None:
        new_position = self.board.get_field(2, 0)
        self.queen.go_to_position(new_position, self.board)
        assert self.queen.position == new_position
        assert new_position.chessman == self.queen

    def test_move_position_not_exist(self) -> None:
        with self.assertRaises(ValueError) as context:
            new_position = self.board.get_field(8, 0)
            self.queen.go_to_position(new_position, self.board)
            self.assertTrue(ValueError in context.exception)

    def test_move_position_not_free_enemy(self) -> None:
        with self.assertRaises(ValueError) as context:
            new_position = self.board.get_field(3, 0)
            Queen(self.board.get_field(1, 0), Color.BLACK)
            self.queen.go_to_position(new_position, self.board)
            self.assertTrue(ValueError in context.exception)

    def test_move_position_enemy(self) -> None:
        new_position = self.board.get_field(2, 0)
        Queen(new_position, Color.BLACK)
        self.queen.go_to_position(new_position, self.board)
        assert self.queen.position == new_position
        assert new_position.chessman == self.queen

    def test_move_position_diagonal(self) -> None:
        row, col = self.queen.position.row, self.queen.position.col
        new_position = self.board.get_field(row + 2, col + 2)
        self.queen.go_to_position(new_position, self.board)
        assert self.queen.position == new_position
        assert new_position.chessman == self.queen

    def test_move_position_enemy_(self) -> None:
        new_position = self.board.get_field(2, 0)
        Queen(new_position, Color.BLACK)
        self.queen.go_to_position(new_position, self.board)
        assert self.queen.position == new_position
        assert new_position.chessman == self.queen

    def test_move_position_not_diagonal(self) -> None:
        row, col = self.queen.position.row, self.queen.position.col
        with self.assertRaises(ValueError) as context:
            new_position = self.board.get_field(row + 2, col + 3)
            self.queen.go_to_position(new_position, self.board)
            self.assertTrue(ValueError in context.exception)

    def test_move_position_not_free_way(self) -> None:
        with self.assertRaises(ValueError) as context:
            new_position = self.board.get_field(3, 0)
            Queen(self.board.get_field(1, 0), Color.WHITE)
            self.queen.go_to_position(new_position, self.board)
            self.assertTrue(ValueError in context.exception)

    def test_move_position_not_free_way_with_enemy(self) -> None:
        with self.assertRaises(ValueError) as context:
            new_position = self.board.get_field(3, 0)
            Queen(self.board.get_field(1, 0), Color.BLACK)
            self.queen.go_to_position(new_position, self.board)
            self.assertTrue(ValueError in context)