class Board:
    def __init__(self):
        self.cells = [" " for _ in range(9)]

    def reset(self):
        self.cells = [" " for _ in range(9)]

    def available_moves(self):
        return [i for i, cell in enumerate(self.cells) if cell == " "]

    def make_move(self, index, player):
        if self.cells[index] == " ":
            self.cells[index] = player
            return True
        return False

    def undo_move(self, index):
        self.cells[index] = " "

    def is_full(self):
        return " " not in self.cells

