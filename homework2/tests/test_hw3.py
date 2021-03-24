from typing import Any, List

import pytest

from homework2.src.hw3 import combinations


@pytest.mark.parametrize(
    ["lists", "expected_result"],
    [
        (([1, 2], [3, 4]), [[1, 3], [1, 4], [2, 3], [2, 4]]),
        (
            ([1, 2, 3], [4], [5, 6]),
            [[1, 4, 5], [1, 4, 6], [2, 4, 5], [2, 4, 6], [3, 4, 5], [3, 4, 6]],
        ),
    ],
)
def test_combinations(lists: List[Any], expected_result: List[List]):
    actual_result = combinations(*lists)

    assert actual_result == expected_result
