"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""

# Sorry, this is a simple but quick solution to the task. Not pythonic in some places :(
# But I'll try to make it better!

from itertools import chain
from typing import List

EMPTY = "-"
DRAW = "draw!"
UNF = "unfinished!"


def check_input_data(board: List[List]) -> list:
    if not all(isinstance(row, list) for row in board):
        raise ValueError("board should be List[List]")

    simple_board = list(chain.from_iterable(board))

    if len(simple_board) != 3 ** 2:
        raise ValueError("board should be 3x3 size")

    return simple_board


def tic_tac_toe_checker(board: List[List]) -> str:
    simple_board = check_input_data(board)

    ways_to_win = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    for row in ways_to_win:
        if (
            simple_board[row[0]]
            == simple_board[row[1]]
            == simple_board[row[2]]
            != EMPTY
        ):
            return f"{simple_board[row[0]]} wins!"
    if EMPTY in simple_board:
        return UNF
    return DRAW
