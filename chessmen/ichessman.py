from abs import ABC, abstractmethod
from .color import Color


class IChessman(ABC):

    @abstractmethod
    def get_position(self):
        pass 

    @abstractmethod
    def new_position(self, row, col, chessfield):
        pass


class BaseChessman(IChessman):

    def __init__(self, row: int, col: int, color: Color):
        self.row = row
        self.col = col
        self.color = color

    def get_position(self):
        return self.row, self.col 

    def is_out_of_field(self, row, col):
        if not (0 <= row <= 7 and 0 <= col <= 7):
            return False 
        return True