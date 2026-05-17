import tkinter as tk
from tkinter import messagebox

from core.game import Game
from ai.difficulty import get_ai_move

from gui.styles import *

game = Game()

buttons = []

current_difficulty = "hard"

root = tk.Tk()
root.title("Tic-Tac-Toe AI")
root.configure(bg=BG_COLOR)

def restart_game():
    game.board.reset()

    for btn in buttons:
        btn.config(text="")

def check_game_status(player):

    if game.check_winner(player):
        messagebox.showinfo("Game Over", f"{player} Wins!")
        restart_game()
        return True

    if game.draw():
        messagebox.showinfo("Game Over", "Draw!")
        restart_game()
        return True

    return False

def ai_turn():

    move = get_ai_move(game, current_difficulty)

    game.board.make_move(move, "O")

    buttons[move].config(text="O")

    check_game_status("O")

def player_move(index):

    if game.board.cells[index] != " ":
        return

    game.board.make_move(index, "X")

    buttons[index].config(text="X")

    if check_game_status("X"):
        return

    ai_turn()

for i in range(9):

    btn = tk.Button(
        root,
        text="",
        width=5,
        height=2,
        bg=BTN_COLOR,
        fg=TEXT_COLOR,
        font=FONT,
        command=lambda i=i: player_move(i)
    )

    btn.grid(row=i//3, column=i%3, padx=5, pady=5)

    buttons.append(btn)

restart_btn = tk.Button(
    root,
    text="Restart",
    command=restart_game
)

restart_btn.grid(row=3, column=0, columnspan=3, sticky="we")

def launch_gui():
    root.mainloop()