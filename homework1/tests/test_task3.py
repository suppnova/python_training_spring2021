import os
from typing import Tuple

import pytest

from homework1.src.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("test_files_task3/pos_test_file.txt", (1, 5)),
        ("test_files_task3/negative_number_test_file.txt", (-1000, 1000)),
        ("test_files_task3/same_numbers_test_file.txt", (5, 5)),
        ("test_files_task3/zeros_test_file.txt", (0, 0)),
    ],
)
def test_find_maximum_and_minimum(file_name: str, expected_result: Tuple):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    actual_result = find_maximum_and_minimum(file_path)

    assert actual_result == expected_result
