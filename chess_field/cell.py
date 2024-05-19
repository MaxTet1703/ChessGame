class ChessCell:

    def __init__(self, row, col):
        self.row = row 
        self.col = col 
        self.is_busy = None

    def retrive_or_free(self, new_master=None):
        self.is_busy = new_master