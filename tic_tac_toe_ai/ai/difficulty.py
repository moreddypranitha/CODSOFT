from ai.random_ai import random_move
from ai.minimax_ai import best_move

def get_ai_move(game, difficulty):

    if difficulty == "easy":
        return random_move(game.board)

    elif difficulty == "hard":
        return best_move(game)

    return best_move(game)