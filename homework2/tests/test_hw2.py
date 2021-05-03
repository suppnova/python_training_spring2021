from typing import List, Tuple

import pytest

from homework2.src.hw2 import major_and_minor_elem


@pytest.mark.parametrize(
    ["values_list", "expected_result"],
    [([3, 2, 3], (3, 2)), ([2, 2, 1, 1, 1, 2, 2], (2, 1))],
)
def test_major_and_minor_elem(values_list: List, expected_result: Tuple[int, int]):
    actual_result = major_and_minor_elem(values_list)

    assert actual_result == expected_result
