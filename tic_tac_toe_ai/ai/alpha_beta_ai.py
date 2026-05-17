import math

def alpha_beta(game, depth, alpha, beta, maximizing):

    if game.check_winner("O"):
        return 1

    if game.check_winner("X"):
        return -1

    if game.draw():
        return 0

    if maximizing:
        value = -math.inf

        for move in game.board.available_moves():

            game.board.make_move(move, "O")

            value = max(
                value,
                alpha_beta(game, depth + 1, alpha, beta, False)
            )

            game.board.undo_move(move)

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = math.inf

        for move in game.board.available_moves():

            game.board.make_move(move, "X")

            value = min(
                value,
                alpha_beta(game, depth + 1, alpha, beta, True)
            )

            game.board.undo_move(move)

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value