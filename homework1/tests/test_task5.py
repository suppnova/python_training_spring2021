from typing import List

import pytest

from homework1.src.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 3, -1, -3, 5, 3, 6, 7], 1, 7),
        ([1, 3, -1, -3, 5, 3, 6, 7], 8, 21),
        ([-1, -1, -1, -1, -1, -1, -1, -1], 3, -1),
        ([1, 3, -1, -3, 5, -30, 6, 7], 3, 13),
    ],
)
def test_sum_of_four(nums: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(nums, k)

    assert actual_result == expected_result
