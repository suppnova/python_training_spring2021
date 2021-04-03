import string
from typing import Iterable, List

import pytest

from homework2.src.hw5 import custom_range


@pytest.mark.parametrize(
    ["iterable_obj", "arguments", "expected_result"],
    [
        (string.ascii_lowercase, "g", ["a", "b", "c", "d", "e", "f"]),
        (
            string.ascii_lowercase,
            ["g", "p"],
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        (string.ascii_lowercase, ["p", "g", -2], ["p", "n", "l", "j", "h"]),
        (string.ascii_letters, ["y", "E"], ["y", "z", "A", "B", "C", "D"]),
    ],
)
def test_custom_range(iterable_obj: Iterable, arguments: List, expected_result: List):
    actual_result = custom_range(iterable_obj, *arguments)

    assert actual_result == expected_result
