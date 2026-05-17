from core.game import Game

def test_winner():

    game = Game()

    game.board.cells = [
        "X", "X", "X",
        " ", "O", " ",
        "O", " ", " "
    ]

    assert game.check_winner("X")