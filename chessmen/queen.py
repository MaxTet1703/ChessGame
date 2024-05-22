from .ichessman import IChessman
from ..board import chessfield


class Queen(IChessman):
   
    def add_move(
            self,
            position: chessfield.ChessField,
            moves: list[chessfield.ChessField],
    ) -> bool:
        chessman = position.chessman
        if chessman:
            if chessman.color != self.color:
                moves.append(position)
            return False
        else:
            moves.append(position)
            return True

    def get_possible_moves(
            self,
            all_position: list[list[chessfield.ChessField]]
    ) -> list[list[chessfield.ChessField]]:
        moves = []
        y = self.position.row
        x = self.position.col
        for i in range(x + 1, 8):
            if not self.add_move(all_position[y][i], moves):
                break

        for i in range(x - 1, -1, -1):
            if not self.add_move(all_position[y][i], moves):
                break

        for i in range(y + 1, 8):
            if not self.add_move(all_position[i][x], moves):
                break

        for i in range(y - 1, -1, -1):
            if not self.add_move(all_position[i][x], moves):
                break

        i = x + 1
        for j in range(y + 1, 8):
            if i < 8:
                if not self.add_move(all_position[j][i], moves):
                    break
                i += 1
            else:
                break

        i = x - 1
        for j in range(y - 1, -1, -1):
            if i >= 0:
                if not self.add_move(all_position[j][i], moves):
                    break
                i -= 1
            else:
                break

        i = x + 1
        for j in range(y - 1, -1, -1):
            if i < 8:
                if not self.add_move(all_position[j][i], moves):
                    break
                i += 1
            else:
                break

        i = x - 1
        for j in range(y + 1, 8):
            if i >= 0:
                if not self.add_move(all_position[j][i], moves):
                    break
                i -= 1
            else:
                break

        return moves
