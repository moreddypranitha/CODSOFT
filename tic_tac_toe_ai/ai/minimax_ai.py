import math

def minimax(game, depth, maximizing):

    if game.check_winner("O"):
        return 1

    if game.check_winner("X"):
        return -1

    if game.draw():
        return 0

    if maximizing:
        best = -math.inf

        for move in game.board.available_moves():
            game.board.make_move(move, "O")

            score = minimax(game, depth + 1, False)

            game.board.undo_move(move)

            best = max(best, score)

        return best

    else:
        best = math.inf

        for move in game.board.available_moves():
            game.board.make_move(move, "X")

            score = minimax(game, depth + 1, True)

            game.board.undo_move(move)

            best = min(best, score)

        return best


def best_move(game):
    best_score = -math.inf
    move = None

    for possible_move in game.board.available_moves():

        game.board.make_move(possible_move, "O")

        score = minimax(game, 0, False)

        game.board.undo_move(possible_move)

        if score > best_score:
            best_score = score
            move = possible_move

    return move