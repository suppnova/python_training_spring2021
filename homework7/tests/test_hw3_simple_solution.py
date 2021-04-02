from typing import List

import pytest

from homework7.src.hw3_simple_solution import tic_tac_toe_checker


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        (([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]), "unfinished!"),
        (([["x", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]), "x wins!"),
        (([["x", "-", "o"], ["-", "x", "o"], ["x", "o", "o"]]), "o wins!"),
        (([["o", "x", "o"], ["x", "x", "x"], ["-", "o", "-"]]), "x wins!"),
        (([["o", "x", "o"], ["x", "x", "o"], ["x", "o", "x"]]), "draw!"),
    ],
)
def test_tic_tac_toe_checker(board: List[List], expected_result: str):
    actual_result = tic_tac_toe_checker(board)
    assert actual_result == expected_result


def test_tic_tac_toe_checker_input_data_value_err():
    with pytest.raises(ValueError):
        tic_tac_toe_checker({("o", "x", "o"), ("x", "x", "o"), ("x", "o", "x")})

    with pytest.raises(ValueError):
        tic_tac_toe_checker([["o", "x", "o"], ["x", "x", "o"], ["x", "o"]])
