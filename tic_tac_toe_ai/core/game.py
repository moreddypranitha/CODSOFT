WIN_COMBINATIONS = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
]

class Game:
    def __init__(self):
        from core.board import Board
        self.board = Board()

    def check_winner(self, player):
        for combo in WIN_COMBINATIONS:
            if all(self.board.cells[i] == player for i in combo):
                return True
        return False

    def draw(self):
        return self.board.is_full()