from typing import Any

import pytest

from homework7.src.hw1 import example_tree, find_occurrences

empty_tree = {}

int_and_bool_tree = {
    "first": [3, 2, False],
    "second": {
        "tuple_key": ("tuple", "with", 3, "and", True, "value"),
    },
    "third": {
        "one": True,
        "two": 2,
        "set": {True, 3},
        "complex_key": {
            "key1": 1,
            "key2": 3,
            "key3": ["a", "lot", "of", "values", {"nested_3": 3, "nested_bool": True}],
        },
    },
    "fourth": 3,
}


@pytest.mark.parametrize(
    ["tree", "element", "expected_result"],
    [
        (example_tree, "RED", 6),
        (empty_tree, "RED", 0),
        (int_and_bool_tree, 3, 6),
        (int_and_bool_tree, True, 4),
        (int_and_bool_tree, 3.0, 0),
    ],
)
def test_find_occurrences(tree: dict, element: Any, expected_result: int):
    assert find_occurrences(tree, element) == expected_result
