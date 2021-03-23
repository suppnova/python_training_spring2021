from typing import Sequence

import pytest

from homework1.src.task02 import check_fib_sequence


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ([], False),
        ([0], True),
        ([10946, 17711], True),
        ([10, 33], False),
        ([2, 3, 5, 8, 13], True),
        ([0, 0, 0, 0, 0], False),
        ((1, 1, 1, 1, 1), False),
        ([0, 1, 1, 2, 5], False),
    ],
)
def test_fib_sequence(data: Sequence[int], expected_result: bool):
    actual_result = check_fib_sequence(data)

    assert actual_result == expected_result
