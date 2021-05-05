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
    n = len(board)

    win_slices = []
    for i in range(0, n ** 2, n):  # add winning strings
        win_slices.append(slice(i, i + n))

    for i in range(n):
        win_slices.append(slice(i, n ** 2, n))  # add winning columns

    win_slices.append(slice(0, n ** 2, n + 1))
    win_slices.append((slice(n - 1, n ** 2 - 1, n - 1)))  # add winning diagonales

    for slice_ in win_slices:
        if len(set(simple_board[slice_])) == 1 and simple_board[slice_][0] != EMPTY:
            return f"{simple_board[slice_][0]} wins!"
    if EMPTY in simple_board:
        return UNF
    return DRAW
